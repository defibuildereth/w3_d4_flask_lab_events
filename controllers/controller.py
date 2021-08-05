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

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_location = request.form['location']
    event_guests = request.form['guests']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, event_guests, event_location, event_description)
    add_new_event(new_event)
    return render_template('index.html', events = events)
