from app.models import db, Web
def seed_webs():

  data = [
          Web(users_id='2', web_title='the smash', web_desc='just some loud smashy music', web_mood='Energetic', web_similarity='', web_genre='', web_era='')
          Web(users_id='6', web_title='study', web_desc='Gotta stay awake to study WITHOUT dancing the night away!', web_mood='Eclectic', web_similarity='', web_genre='', web_era='')
          Web(users_id='2', web_title='late night', web_desc='', web_mood='Netflix', web_similarity='', web_genre='', web_era='')
          Web(users_id='1', web_title='morning wakeup', web_desc='', web_mood='Happy', web_similarity='', web_genre='', web_era='')
          Web(users_id='1', web_title='gotta move', web_desc='shake that groove thang', web_mood='', web_similarity='', web_genre='', web_era='70's')
          Web(users_id='7', web_title='super chill', web_desc='', web_mood='Chill', web_similarity='', web_genre='R&B', web_era='')
          Web(users_id='3', web_title='moments of quiet', web_desc='', web_mood='Chill', web_similarity='', web_genre='', web_era='')
          Web(users_id='4', web_title='breakup', web_desc='this sucks! Hate her', web_mood='Sad', web_similarity='', web_genre='', web_era='')
          Web(users_id='4', web_title='love', web_desc='So in love', web_mood='Happy', web_similarity='', web_genre='', web_era='')
          Web(users_id='5', web_title='life soundtrack', web_desc='soundtrack of my life', web_mood='', web_similarity='', web_genre='', web_era='')
  ]
  for web in data:
        user.webs.append(web)
        db.session.add(web)
    db.session.commit()

def undo_webs():
    db.session.execute('TRUNCATE webs RESTART IDENTITY CASCADE;')
    db.session.commit()