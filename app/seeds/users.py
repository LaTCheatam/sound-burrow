# from werkzeug.security import generate_password_hash
from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():

    data = [
        User(full_name='Demo Waters', username='Demo', email='demo@aa.io', avatar='',
                password='password')
        User(full_name='Sarah Shane', username='sshane', email='sshane@aa.io', avatar='',
                password='password')
        User(full_name='Niko Nos', username='niknos', email='niknos@aa.io', avatar='',
                password='password')
        User(full_name='Fae Octo', username='Cep', email='cep@aa.io', avatar='',
                password='password')
        User(full_name='Sunshyne Collins', username='sundoesshyne', email='dasunshyne@aa.io', avatar='',
                password='password')
        User(full_name='Simm Simmons', username='SimSimma', email='simma@aa.io', avatar='',
                password='password')
        User(full_name='George Ronson', username='Grons', email='grons@aa.io', avatar='',
                password='password')
        User(full_name='Zack Bane', username='Zaban', email='Zaban@aa.io', avatar='',
                password='password')
    ]

    for user in data:
        db.session.add(user)
    db.session.commit()

def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()