from flask.cli import AppGroup
from .users import seed_users, undo_users
from .musics import seed_musics, undo_musics
from app.models import db

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    db.drop_all()
    db.create_all()
    seed_users()
    seed_musics()

    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
