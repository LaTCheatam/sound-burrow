from re import S
from flask_wtf import FlaskForm
from wtforms.fields import (PasswordField, SelectField, StringField, SubmitField, DateTimeField, IntegerField)  # noqa
from wtforms.fields.core import BooleanField, DateTimeField


class UpdateForm(FlaskForm):
  full_name = StringField("Full Name")
  username = StringField("Username")
  email = ('Email')
  avatar = ('Avatar')