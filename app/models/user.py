from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  full_name = db.Column(db.String(40), nullable = False)
  username = db.Column(db.String(40), nullable = False, unique = True)
  email = db.Column(db.String(255), nullable = False, unique = True)
  hashed_password = db.Column(db.String(255), nullable = False)
  avatar = db.Column(db.String(2000), nullable = True)
  created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())

  webs = db.relationship("Web", back_populates="creator")
  playlists = db.relationship("Playlist", back_populates="author")

  @property
  def password(self):
    return self.hashed_password


  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)


  def check_password(self, password):
    return check_password_hash(self.password, password)


  def to_dict(self):
    return {
      "id": self.id,
      "full_name": self.full_name,
      "username": self.username,
      "email": self.email,
      "avatar": self.avatar,
      "created_at": self.created_at
  }
