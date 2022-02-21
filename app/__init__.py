from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY']='madd!3'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='username'
app.config['MAIL_PASSWORD']='password'
app.config.from_object(Config)
csrf = CSRFProtect(app)



mail = Mail(app)
from app import views
