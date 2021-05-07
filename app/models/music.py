from app.models import music_playlist, music_web
from .db import db
from sqlalchemy.sql import func
from .web import Music_Web
from .playlist import Music_Playlist

class Music(db.Model):
    __tablename__ = "musics"

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    artist = db.Column(db.String(40), nullable=False)
    song_title = db.Column(db.String(40), nullable=False)
    song_mood = db.Column(db.String(40), nullable=False)
    song_similarity = db.Column(db.String(40), nullable=False)
    song_genre = db.Column(db.String(40), nullable=False)
    song_era = db.Column(db.String(40), nullable=False)

    webs = db.relationship("Web", secondary=Music_Web, back_populates="musics")
    webs = db.relationship("Playlist", secondary=music_playlist.Music_Playlist, back_populates="musics")
      
    def to_dict(self):
        return {
        "id": self.id,
        "artist": self.web_name,
        "users_id": self.users_id,
        "song_title": self.song_title,
        "song_mood": self.song_mood,
        "song_similarity": self.song_similarity,
        "song_genre": self.song_genre,
        "song_era": self.song_era,
        "createdAt": self.createdAt,
        "updatedAt": self.updatedAt
            }