from models.event import Event

event_1 = Event('6th August 2021', 'Fantastic Frolic Finds Focal Face', 5, 'udderbelly', 'alliterative fun with friends')
event_2 = Event('7th August 2021', 'Great Game Gets Goalies Grateful', 28, 'Tynecastle', 'bunch of grateful goalies, what could be finer')
event_3 = Event('8th August 2021', 'Heavy Hippopotamai Hold Harry Hostage', 14, 'Edinburgh Dungeon', 'poor harry has got himself in quite a pickle this time')

events = [event_1, event_2, event_3]

def add_new_event(event):
    events.append(event)