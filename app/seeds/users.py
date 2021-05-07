# from werkzeug.security import generate_password_hash
from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():

    data = [
        User(full_name='Demo Waters', username='Demo', email='demo@aa.io', avatar='https://depositphotos.com/53329667/stock-illustration-businessman-back-view.html', password='password'),
        User(full_name='Sarah Shane', username='sshane', email='sshane@aa.io', avatar='https://depositphotos.com/90095920/stock-illustration-albert-einstein-head.html',password='password'),
        User(full_name='Niko Nos', username='niknos', email='niknos@aa.io', avatar='https://depositphotos.com/18717899/stock-illustration-cute-green-face-vector-illustration.html',password='password'),
        User(full_name='Fae Octo', username='Cep', email='cep@aa.io', avatar='https://depositphotos.com/42482651/stock-illustration-beautiful-woman.html', password='password'),
        User(full_name='Sunshyne Collins', username='sundoesshyne', email='dasunshyne@aa.io', avatar='https://depositphotos.com/56695433/stock-illustration-female-avatar.html', password='password'),
        User(full_name='Simm Simmons', username='SimSimma', email='simma@aa.io', avatar='https://depositphotos.com/18937707/stock-illustration-little-panda-bamboo-vector-illustration.html', password='password'),
        User(full_name='George Ronson', username='Grons', email='grons@aa.io', avatar='https://depositphotos.com/vector-images/avatar.html?filter=illustration&search_params=eyJjdGYiOiIxIiwiZlthdWRpb10iOjAsImZbYXVkaW9fdHlwZV0iOm51bGx9', password='password'),
        User(full_name='Zack Bane', username='Zaban', email='Zaban@aa.io', avatar='https://depositphotos.com/18468391/stock-illustration-vector-user-icon.html',
                password='password'),
    ]

    for user in data:
        db.session.add(user),
    db.session.commit(),

def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;'),
    db.session.commit(),