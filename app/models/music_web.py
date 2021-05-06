from .db import db

Music_Web = db.Table(
  "music_webs",
  web_id = db.Column("web_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
  playlist_id = db.Column("playlistId", db.Integer, db.ForeignKey("playlists.id"), primary_key=True)
)