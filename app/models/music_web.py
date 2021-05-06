from .db import db

Music_Web = db.Table(
  "music_webs",
  web_id = db.Column("web_id", db.Integer, db.ForeignKey("web.id")),
  music_id = db.Column("music_id", db.Integer, db.ForeignKey("music.id"))
)