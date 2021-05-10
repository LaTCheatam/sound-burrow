from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import current_user, login_required
from app.models import Playlist
from app.models import Web
from app.models import Music
from app.models import User
from app.models import music_web
from app.models import db

web_routes = Blueprint('webs', __name__)

# create web - on successful save redirect to webs_routes.route('/webs/int:id', methods=['GET'])
# @web_routes.route('/create', methods=['POST'])
# def create_web(id):
  # form = CreateWebForm()
  # form['csrf_token'].data = request.cookies['csrf_token']
  # user = User.query.get(id)

#add song or artist to 
# @web_routes.route('/<int:id>/add', methods=['PATCH'])

# display single webs page
@web_routes.route('/<int:id>', methods=['GET']) 
def get_web(id):
  web = Web.query.get(id)
  return web.to_dict()


# get all of a users webs listed on page.
@web_routes.route('/', methods=['GET']) 
def get_webs(id):
    user = User.query.get(id)
    webs = Web.query.filter(Web.users_id).order_by(Web.web_name.desc()).all
    return {
        "The Webs": [webs.to_dict() for web in webs]
    }

# delete a web
@web_routes.route('/<int:id>/delete', methods=['DELETE']) 
def delete_web(id):
  web = Web.query.get(id)
  db.session.delete(web)
  db.session.commit()
  return f'Web: "{web.web_name}" is no more.'

# update a web
# @web_routes.route('/<int:id>/update', methods=['PUT']) 
# def update_web(id):
#   web = Web.query.get(id)
#   if web:
#     web.web_name = request.form['web_name']
#     web.web_mood = request.form['web_mood']
#     web.web_similarity = request.form['web_similarity']
#     web.web_genre = request.form['web_genre']
#     web.web_era = request.form['web_er']
#     return f'{Web} successfully updated'