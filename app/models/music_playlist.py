from .db import db

music_playlist = db.Table(
  "music_playlists",

  db.Column(
    "playlist_id", 
    db.Integer, 
    db.ForeignKey("playlists.id"), 
    primary_key=True),
  db.Column(
    "music_id", 
    db.Integer, 
    db.ForeignKey("musics.id"), 
    primary_key=True)
)