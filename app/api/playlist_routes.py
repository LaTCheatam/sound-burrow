from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import Playlist
from app.models import Web
from app.models import Music
from app.models import User
from app.models import Music_Playlist

# create web - on successful save redirect to playlists_routes.route('/playlist/int:id', methods=['GET'])
playlists_routes.route('/playlist/create', methods=['POST']) 

# display single playlists page
playlists_routes.route('/playlist/int:id', methods=['GET']) 

# get all of a users playlists listed on page.
playlists_routes.route('/users/int:id/playlists', methods=['GET']) 

# delete a playlist
playlists_routes.route('/playlists/int:id/delete', methods=['DELETE']) 

 # update a playlists if successful redirect to playlists_routes.route('/playlist/int:id', methods=['GET'])
playlists_routes.route('/playlists/int:id/update', methods=['PUT'])