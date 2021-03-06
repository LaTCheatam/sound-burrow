from .db import db
from sqlalchemy.sql import func
from app.models import music_web

class Web(db.Model):
  __tablename__ = "webs"

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  web_name = db.Column(db.String(100), nullable=False)
  web_desc = db.Column(db.String(), nullable=False)
  users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  web_mood = db.Column(db.String(100), nullable=True)
  web_similarity = db.Column(db.String(100), nullable=True)
  web_genre = db.Column(db.String(100), nullable=True)
  web_era = db.Column(db.String(100), nullable=True)
  created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
  created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())

  creator = db.relationship("User", back_populates="webs", uselist = False)
  musics = db.relationship("Music", secondary="music_webs", back_populates="webs")

  def to_dict(self):
    return {
      "id": self.id,
      "web_name": self.web_name,
      "users_id": self.users_id,
      "web_mood": self.web_mood,
      "web_similarity": self.web_similarity,
      "web_genre": self.web_genre,
      "web_era": self.web_era,
      "created_at": self.created_at,
      "updated_at": self.updated_at
    }
