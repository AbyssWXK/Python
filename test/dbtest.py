# coding:utf-8
import os
from flask import Flask, render_template, session, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql://root:112358@localhost/music'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Music(db.Model):
    __tablename__ = 'musiclist'
    id = db.Column(db.Integer, primary_key=True)
    musicname = db.Column(db.VARCHAR(45), unique=True)
    em1 = db.Column(db.Float, unique=True)
    em2 = db.Column(db.Float, unique=True)
    em3 = db.Column(db.Float, unique=True)
    em4 = db.Column(db.Float, unique=True)
    em5 = db.Column(db.Float, unique=True)
    em6 = db.Column(db.Float, unique=True)
    em7 = db.Column(db.Float, unique=True)
    em8 = db.Column(db.Float, unique=True)
    em9 = db.Column(db.Float, unique=True)
    em10 = db.Column(db.Float, unique=True)
    def __init__(self, musicname, em1, em2, em3, em4, em5, em6, em7, em8, em9, em10):
        self.musicname = musicname
        self.em1 = em1
        self.em2 = em2
        self.em3 = em3
        self.em4 = em4
        self.em5 = em5
        self.em6 = em6
        self.em7 = em7
        self.em8 = em8
        self.em9 = em9
        self.em10 = em10
    def __repr__(self):
        return '<Music %r %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f>' %  \
               (self.musicname, self.em1, self.em2, self.em3, self.em4, self.em5, self.em6, self.em7, self.em8, self.em9, self.em10)
ma = Music('myheart',1,2,3,1,1,2,1,3,1,2)
print ma
db.session.add(ma)
db.session.commit()