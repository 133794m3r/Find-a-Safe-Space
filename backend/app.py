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
print(MYSQL_CREDS)
engine = create_engine(MYSQL_CREDS)
db = scoped_session(sessionmaker(bind=engine))
#
# mongo = PyMongo(app)



@app.route('/')
def index():
	return app.send_static_file('home.html')

@app.route('/schedule')
def schedule():
	return render_template('schedule.html')
	pass

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