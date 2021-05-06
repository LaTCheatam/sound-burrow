from .db import db
from sqlalchemy.sql import func

class Playlist(db.Model):
  __tablename__ = "playlists"

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  pl_title = db.Column(db.String(40), nullable=False)
  pl_desc = db.Column(db.String(40), nullable=True)
  pl_mood = db.Column(db.String(40), nullable=True)
  pl_similarity = db.Column(db.String(40), nullable=True)
  pl_genre = db.Column(db.String(40), nullable=True)
  pl_era = db.Column(db.String(40), nullable=True)
  created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())

  def to_dict(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "pl_title": self.pl_title,
            "pl_mood": self.pl_mood,
            "pl_similarity": self.pl_similarity,
            "pl_genre": self.pl_genre,
            "pl_era": self.pl_era,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }