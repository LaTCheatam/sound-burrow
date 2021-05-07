from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import Playlist
from app.models import Web
from app.models import Music
from app.models import User
from app.models import Music_Web

# create web - on successful save redirect to webs_routes.route('/webs/int:id', methods=['GET'])
webs_routes.route('/webs/create', methods=['POST']) 

# display single webs page
webs_routes.route('/webs/int:id', methods=['GET']) 

# get all of a users webs listed on page.
webs_routes.route('/users/int:id/webs', methods=['GET']) 

# delete a web
webs_routes.route('/webs/int:id/delete', methods=['DELETE']) 

# update a web
webs_routes.route('/webs/int:id/update', methods=['PUT']) 