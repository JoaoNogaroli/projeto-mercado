from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ualklbiwizwanb:8edfe73ae7d8fdb7a4dcf562227a2d38a606e6bbd973aa8863dd8caeeeba15ed@ec2-34-233-0-64.compute-1.amazonaws.com:5432/de0mgancm0n9ld'
app.config['SECRET_KEY']= 'qwgy14'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)