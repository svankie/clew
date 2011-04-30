from flask.globals import request
from flask.templating import render_template

from clew.core.model import Event
from clew.search.searcher import EventSearcher

__author__ = 'svankiE'

from clew import app

# TESTING.-
@app.route("/search", methods=['GET'])
def search():
    es = EventSearcher()
    results = es.search(request.args.get('search_query', ""))
    return results

# EVENT VIEWS
@app.route('/', methods=['GET', 'POST'])
def get_or_post_events():
    if request.method == 'GET':
        events = Event.query.all()
        return render_template('index.html', events=events)
    if request.method == 'POST':
        pass
    else:
        pass

@app.route('/events/<event_id>', methods=['GET'])
def get_event(event_id):
    pass

@app.route('/events/<event_id>', methods=['PUT', 'DELETE'])
def put_or_delete_event(event_id):
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    else:
        pass

# ARTIST VIEWS
@app.route('/artists', methods=['GET', 'POST'])
def get_or_post_artists():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    else:
        pass

@app.route('/artists/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    pass

@app.route('/artists/<artist_id>', methods=['PUT', 'DELETE'])
def put_or_delete_artist(artist_id):
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    else:
        pass

# VENUE VIEWS
@app.route('/venues', methods=['GET', 'POST'])
def get_or_post_venues():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    else:
        pass

@app.route('/venues/<venue_id>', methods=['GET'])
def get_venue(venue_id):
    pass

@app.route('/venues/<venue_id>', methods=['PUT', 'DELETE'])
def put_or_delete_venue(venue_id):
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    else:
        pass

# AGENDA VIEWS
@app.route('/agenda', methods=['GET', 'POST'])
def get_or_post_agenda():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    else:
        pass

@app.route('/agenda/<agenda_id>', methods=['PUT', 'DELETE'])
def put_or_delete_agenda(agenda_id):
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    else:
        pass

# USER VIEWS
@app.route('/users', methods=['GET', 'POST'])
def get_or_post_users():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    else:
        pass
        
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    pass

@app.route('/users/<user_id>', methods=['PUT', 'DELETE'])
def put_or_delete_user(user_id):
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    else:
        pass

# SHOUT VIEWS
@app.route('/events/<event_id>/shouts', methods=['GET', 'POST'])
def get_or_post_shouts(event_id):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    else:
        pass
    
@app.route('/events/<event_id>/shouts/<shout_id>', methods=['GET'])
def get_shout(event_id, shout_id):
    pass

@app.route('/events/<event_id>/shouts/<shout_id>', methods=['DELETE'])
def delete_shout(event_id, shout_id):
    pass

# INVITATION VIEWS
@app.route('/events/<event_id>/invitations', methods=['GET', 'POST'])
def get_or_post_invitations(event_id):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    else:
        pass
    
@app.route('/events/<event_id>/invitations/<invitation_id>', methods=['GET'])
def get_invitation(event_id, invitation_id):
    pass

@app.route('/events/<event_id>/invitations/<invitation_id>', methods=['PUT', 'DELETE'])
def put_or_delete_invitation(event_id, invitation_id):
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    else:
        pass

# WISHLIST VIEWS
@app.route('/users/<user_id>/wishlist', methods=['GET'])
def get_wishlist(user_id):
    pass

# LOOPING SEARCH VIEWS
@app.route('/users/<user_id>/wishlist/ls', methods=['GET', 'POST'])
def get_or_post_ls(user_id):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    else:
        pass

@app.route('/users/<user_id>/wishlist/ls/<ls_id>', methods=['DELETE', 'PUT'])
def put_or_delete_ls(user_id, ls_id):
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    else:
        pass
    