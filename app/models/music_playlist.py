from .db import db

Music_Playlist = db.Table(
  "music_playlists",
  playlist_id = db.Column("playlist_id", db.Integer, db.ForeignKey("playlists.id"), primary_key=True),
  music_id = db.Column("music_id", db.Integer, db.ForeignKey("music.id"), primary_key=True)
)