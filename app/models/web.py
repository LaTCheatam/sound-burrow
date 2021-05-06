from .db import db
from sqlalchemy.sql import func

class Web(db.Model):
  __tablename__ = "webs"

  id = db.Column(db.Integer, nullable=False, primary_key=True)
  web_name = db.Column(db.String(40), nullable=False)
  users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())

  def to_dict(self):
        return {
            "id": self.id,
            "web_name": self.web_name,
            "users_id": self.users_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }