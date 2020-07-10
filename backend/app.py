from flask import Flask,session,render_template,redirect,abort,url_for,request, Response,jsonify
from flask_session import Session
from flask_pymongo import PyMongo
import json
#from . import eliza
import eliza

#from json import loads as json_parse
def init_session(name):
    session['handle']=name
    session['eliza']=eliza.Eliza()
    session['eliza'].load('doctor.txt')
    return session['eliza'].initial()

app = Flask(__name__)
app.config.from_pyfile('config.py')
Session(app)


mongo = PyMongo(app)



@app.route('/')
def index():
    return app.send_static_file('home.html')

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
        if "COVID19_RESP" in response_msg:
            country=get_country(request.remote_addr)
            if country == "United States":
                emergency_info = " <a href='https://www.cdc.gov/coronavirus/2019-ncov/index.html'>CDC COVID19 Home Page</a>"
            else:
                emergency_info = " <a href='https://www.who.int/health-topics/coronavirus'>WHO COVID19 Home Page</a>"

            response_msg = response_msg[13:] + emergency_info
        elif "SUICIDE_RESP" in response_msg:
            emergency_info=crisis_info(request.remote_addr)
            response_msg = response_msg[13:] +" "+ emergency_info

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