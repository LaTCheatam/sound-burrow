from app.models import db, Playlist

def seed_playlists():
    data = [
          Playlist(users_id='2', pl_title='the smash', pl_desc='just some loud smashy music', pl_mood='Energetic', pl_similarity='', pl_genre='', pl_era=''),
          Playlist(users_id='6', pl_title='study', pl_desc='Gotta stay awake to study WITHOUT dancing the night away!', pl_mood='Eclectic', pl_similarity='', pl_genre='', pl_era=''),
          Playlist(users_id='2', pl_title='late night', pl_desc='', pl_mood='Netflix', pl_similarity='', pl_genre='', pl_era=''),
          Playlist(users_id='1', pl_title='morning wakeup', pl_desc='', pl_mood='Happy', pl_similarity='', pl_genre='', pl_era=''),
          Playlist(users_id='1', pl_title='gotta move', pl_desc='shake that groove thang', pl_mood='', pl_similarity='', pl_genre='', pl_era="70's"),
          Playlist(users_id='7', pl_title='super chill', pl_desc='', pl_mood='Chill', pl_similarity='', pl_genre='R&B', pl_era=''),
          Playlist(users_id='3', pl_title='moments of quiet', pl_desc='', pl_mood='Chill', pl_similarity='', pl_genre='', pl_era=''),
          Playlist(users_id='4', pl_title='breakup', pl_desc='this sucks! Hate her', pl_mood='Sad', pl_similarity='', pl_genre='', pl_era=''),
          Playlist(users_id='4', pl_title='love', pl_desc='So in love', pl_mood='Happy', pl_similarity='', pl_genre='', pl_era=''),
          Playlist(users_id='5', pl_title='life soundtrack', pl_desc='soundtrack of my life', pl_mood='', pl_similarity='', pl_genre='', pl_era='')
  ]
    for playlist in data:
        db.session.add(playlist)
    db.session.commit()

def undo_playlists():
    db.session.execute('TRUNCATE playlists RESTART IDENTITY CASCADE;')
    db.session.commit()