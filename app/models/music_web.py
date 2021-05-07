from .db import db

music_web = db.Table(
  "music_webs",
  
  db.Column(
    "web_id", 
    db.Integer, 
    db.ForeignKey("webs.id"), 
    primary_key=True),
  db.Column(
    "music_id", 
    db.Integer, 
    db.ForeignKey("musics.id"), 
    primary_key=True)
)