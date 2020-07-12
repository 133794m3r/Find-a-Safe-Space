from flask import Flask,session,render_template,redirect,abort,url_for,request, Response,jsonify
from flask_session import Session
from flask_pymongo import PyMongo
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import json
#from . import eliza
import eliza
from config import *

#from json import loads as json_parse
def init_session(name):
	session['handle']=name
	session['eliza']=eliza.Eliza()
	session['eliza'].load('doctor.txt')
	return session['eliza'].initial()

app = Flask(__name__)
app.config.from_pyfile('config.py')
Session(app)
engine = create_engine(PSQL_CREDS)
db = scoped_session(sessionmaker(bind=engine))
#
# mongo = PyMongo(app)

def dict_proxy(result_proxy):
	#return [{column: value for column, value in rowproxy.items()} for rowproxy in result_proxy]
	return [{**row} for row in result_proxy]

@app.route('/')
def index():
	return app.send_static_file('home.html')

@app.route('/rsvp/<event_id>/<reservation_uid>',methods=['POST','GET'])
@app.route('/rsvp/<event_id>',methods=['POST','GET'],defaults={'reservation_uid':None})
def rsvp(event_id,reservation_uid):
	import datetime
	from hashlib import sha1
	import base64
	import secrets
	result = db.execute('select * from event_schedules where uid = :uid',
	                    {'uid': event_id}).fetchall()
	data = dict_proxy(result)
	if data:
		data = data[0]
	else:
		return render_template('schedule.html', data=None)
	if request.method == 'POST':
		option = request.form.get('rsvp_option')
		if option == 'yes':
			choice = 1
		elif option == 'no':
			choice = 2
		elif option == 'maybe':
			choice = 3
		else:
			return render_template('rsvp.html',data=None)
		name = request.form.get('name')
		hash_str = str(datetime.datetime.now()).encode('utf-8') + secrets.token_bytes(3)
		reservation_uid = base64.urlsafe_b64encode(sha1(hash_str).digest()).decode('utf-8')
		db.execute('insert into user_reservations(event_id,choice,name,reservation_uid) values(:event_id,:choice,:name,:reservation_uid)',
		           { 'event_id':session['event_id'],'choice':choice,'name':name,'reservation_uid':reservation_uid})
		db.execute(f'update event_schedules set {option} = {option} + 1 where uid = :uid',{'option':option,'uid':event_id})
		db.commit()
		data['reservation_uid'] = reservation_uid
		data['name'] = name
		data[option] += 1
	else:
		if reservation_uid is None:
			data['reservation_uid'] = ''
		else:
			data2 = db.execute('select * from user_reservations where reservation_uid = :reservation_uid')
			dict_proxy(data2)
			data = {**data, **data2}

	session['event_id'] = data['uid']
	data['timestamp'] = datetime.datetime.fromtimestamp(int(data['start_time']))
	print(data)
	return render_template('rsvp.html',data=data)

@app.route('/schedule',defaults={'event_id':None,'event_pass':None},methods = ['POST', 'GET'])
@app.route('/schedule/<event_id>',defaults={'event_pass':None},methods = ['Post','GET'])
@app.route('/schedule/<event_id>/<event_pass>',methods=['POST','GET'])
def schedule(event_id,event_pass):
	print(event_id)
	print(event_pass)
	if request.method == "POST":
		import datetime
		import hashlib
		import secrets
		import base64
		host_name = request.form.get('host_name')
		title = request.form.get('event_title')
		event_location  = request.form.get('event_location')
		start_date = request.form.get('start_date')
		start_time = request.form.get('event_time')
		password = request.form.get('password')
		user_tz = int(request.form.get('user_tz'))
		print('ut',request.form.get('user_time'))
		hash_str = (title+request.form.get('user_time'))+str(datetime.datetime.now())+request.form.get('user_tz')
		hash_str = hash_str.encode('utf-8')
		time_stamp = datetime.datetime.fromtimestamp(int(request.form.get('user_time'))/1000)
		time_stamp = time_stamp + datetime.timedelta(hours=user_tz)
		time_stamp = time_stamp.timestamp()

		uid = base64.urlsafe_b64encode(hashlib.sha1(hash_str+secrets.token_bytes(4)).digest()).decode('utf-8')
		edit_pass = base64.urlsafe_b64encode(hashlib.sha1(hash_str+secrets.token_bytes(4)).digest()).decode('utf-8')
		description = request.form.get('event_description')

		print(uid)
		result = db.execute('''insert into event_schedules(uid,start_time,event_location,event_description,title,password,edit_pass,host_name) values(:uid,:start_time,:event_location,:event_description,:title,:password,:edit_pass,:host_name)''',
		                    {'uid':uid, 'start_time':time_stamp, 'password':password, 'title':title,
		                     'event_location':event_location, 'event_description':description, 'edit_pass':edit_pass,
		                     'host_name':host_name})
		print(result)
		db.commit()
		result = db.execute('select * from event_schedules where uid = :uid',{'uid':uid}).fetchall()
		data = dict_proxy(result)[0]
		data['url'] = request.url_root
		return render_template('schedule.html',data=data)
		#return redirect('/schedule/'+uid+'/'+edit_pass)
	elif event_id is not None and event_pass is not None:
		result = db.execute('select * from event_schedules where uid = :uid and edit_pass = :edit_pass',{'uid':event_id,'edit_pass':event_pass}).fetchall()
		data = dict_proxy(result)
		if data:
			data = data[0]
		else:
			return render_template('schedule.html', data=None)

		data['url'] = request.url_root
		print(data)
		return render_template('schedule.html',data=data)
	else:
		return render_template('schedule.html',data=None)



@app.route('/about')
def about():
	return app.send_static_file('about.html')

@app.route('/msg',methods=["POST","GET"])
def msg():
	user_msg=''
	user_data={}
	response_msg=''
	if request.method == "GET":
		if len(request.args) > 0:
			if session.get('handle') is None:
				name=request.args.get('name')
				response_msg=init_session(name)
			else:
				response_msg=session['eliza'].respond(request.args.get('msg'))
		else:
			return "nothing received"

	else:
		user_data=request.get_json()
		if session.get('handle') is None:
			response_msg=init_session(user_data.get('name'))
		else:
			#if request.form.get('msg') is not None:
			response_msg=session['eliza'].respond(user_data.get('msg'))

	return jsonify({'name':'Eliza','msg':response_msg})


@app.route('/chat')
def chat():
	#session.clear()
	return app.send_static_file('chat.html')

if __name__ == '__main__':
	app.SECRET_KEY = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	sess.init_app(app)
	app.secret_key = 'super secret key'
	app.run(debug=true,SECRET_KEY="secret")
else:
	application = app