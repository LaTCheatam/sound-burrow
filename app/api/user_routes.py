from flask import Blueprint, jsonify, redirect
from flask.globals import request
from flask_login import login_required
from ..models.user import User
from ..models.db import db
from ..models.web import Web
from ..models.playlist import Playlist
from ..forms.update_form import UpdateForm

user_routes = Blueprint('users', __name__)


# @user_routes.route('/')
# @login_required
# def users():
#     users = User.query.all()
#     return {"users": [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


# user webs - user's webs view
@user_routes.route('/int:id/webs', methods=['GET']) 
@login_required
def get_webs(id):
    webs = Web.query.all(id).order_by(Web.web_name.desc())

# user webs - user's webs view
@user_routes.route('/int:id/playlists', methods=['GET']) 
@login_required
def get_playlists(id):
    webs = Playlist.query.all(id).order_by(Playlist.pl_title.desc())

# delete a user -- successful deletion redirect to auth_routes.route('/') -- splash page
@user_routes.route('/int:id/delete', methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit() 
    return redirect('/') 

# update update if successful redirect to user_routes.route('/int:id/dashboard', methods=['GET'])
@user_routes.route('/int:id/update', methods=['PATCH'])
@login_required
def edit_user(id):
    form = UpdateForm
    user = User.query.get(id)
    if user:
        user.full_name = request.form['full_name']
        user.username = request.form['username']
        user.email = request.form['email']
        user.avatar = request.form['avatar']
       

