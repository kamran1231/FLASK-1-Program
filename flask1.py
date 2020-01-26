# from flask import Flask,render_template
#
# app = Flask(__name__, template_folder='templates')
#
# @app.route('/')
#
# def hello():
#     return render_template('index.html')
#
#
# @app.route('/kamran')
#
# def kamran():
#     return 'hello kamran bhai!'
#
# app.run(debug= True)



from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import json
#
# with open('config.json','r') as c:
#     params = json.load(c)['params']

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/aikablog'
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/about')

def about():
    return render_template('about.html')


@app.route('/contact',methods=["GET","POST"])

def contact():

    if (request.method == 'POST'):
        '''Add entry to the database'''

        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name = name,email = email,phone_num = phone,mes = message,date = datetime.now())

        db.session.add(entry)
        db.session.commit()




    return render_template('contact.html')

app.run(debug= True)