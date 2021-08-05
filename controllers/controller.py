from models.event import Event
from models.event_list import *
from flask import render_template, request
from app import app

@app.route('/events')
def index():
    return render_template('index.html', events = events)

@app.route('/events/new')
def new_event():
    return render_template('new.html')