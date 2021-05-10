from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import Playlist
from app.models import Web
from app.models import Music
from app.models import User
from app.models import Music_Playlist
from app.models import db

playlist_routes = Blueprint('playlists', __name__)

# create web - on successful save redirect to playlists_routes.route('/playlist/int:id', methods=['GET'])
playlist_routes.route('/playlist/create', methods=['POST']) 

playlist_routes.route('/playlist/add', methods=['PATCH']) 

# display single playlists page
playlist_routes.route('/playlist/int:id', methods=['GET']) 
def get_playlist(id):
  playlist = Playlist.query.get(id)
  return playlist.to_dict()

# get all of a users playlist listed on page.
playlist_routes.route('/users/int:id/playlists', methods=['GET']) 
def get_playlists(id):
    user = User.query.get(id)
    playlists = Playlist.query.filter(Playlist.users_id).order_by(Playlist.playlist_name.desc()).all
    return {
        "The Playlists": [playlists.to_dict() for playlist in playlists]
    }


# delete a playlist
playlist_routes.route('/playlist/int:id/delete', methods=['DELETE'])
def delete_playlist(id):
  playlist = Playlist.query.get(id)
  db.session.delete(playlist)
  db.session.commit()
  return f'Playlist: "{playlist.playlist_name}" is no more.' 

 # update a playlist if successful redirect to playlist_routes.route('/playlist/int:id', methods=['GET'])
# @playlist_routes.route('/playlist/int:id/update', methods=['PATCH'])
# def update_playlist(id):
#   playlist = Playlist.query.get(id)
#   data = request.data
#   if playlist:
#     playlist.pl_title=request.data
#     playlist.pl_mood=request.data
#     playlist.pl_similarity=request.data
#     playlist.pl_genre=request.data
#     playlist.pl_era=request.data
#     return f'{Playlist} successfully updated'