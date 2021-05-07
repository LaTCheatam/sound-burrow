from app.models import db, Music

def seed_musics():

  data = [
    Music(artist='Abbi Glines', song_title='Fallen Too Far', song_mood='Love', song_similarity='Chill', song_genre='Pop', song_era='2010')
    Music(artist='Adele', song_title='Don't You Remember', song_mood='Melancholy', song_similarity='Edgy Love', song_genre='Pop', song_era='2010')
    Music(artist='Adele', song_title='He Won't Go', song_mood='Breakup', song_similarity='Edgy Love', song_genre='Pop', song_era='2010')
    Music(artist='Adele', song_title='I Found a Boy', song_mood='Breakup', song_similarity='Edgy Love', song_genre='Pop', song_era='2010')
    Music(artist='Anthony Hamilton', song_title='Woo', song_mood='Lust', song_similarity='Funky Love', song_genre='R&B Soul', song_era='2010')
    Music(artist='Antibala', song_title='Dirty Money', song_mood='Upbeat', song_similarity='Electronic Funk', song_genre='World', song_era='2010')
    Music(artist='Bastille', song_title='Pompeii', song_mood='Upbeat', song_similarity='Alternative', song_genre='Alternative', song_era='2010')
    Music(artist='Beyoncé', song_title='Haunted', song_mood='Dark', song_similarity='Edgy', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Drunk in Love (feat. Jay Z', song_mood='Dance', song_similarity='Love', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Blow', song_mood='Upbeat', song_similarity='Lust', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='No Angel', song_mood='Dark', song_similarity='Edgy Love', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='6 Inch feat. The Weekend', song_mood='Sexy', song_similarity='Edgy', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Pray You Catch Me', song_mood='Ethereal', song_similarity='Chill', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Don't Hurt Yourself (feat. Jack White', song_mood='Dark', song_similarity='Edgy Love', song_genre='Rock', song_era='2010')
    Music(artist='Beyoncé', song_title='Hold Up', song_mood='Breakup', song_similarity='Edgy Love', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Sorry', song_mood='Breakup', song_similarity='Edgy Love', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Daddy Lessons', song_mood='Revival', song_similarity='Dance', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Sandcastles', song_mood='Breakup', song_similarity='Love', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='All Night', song_mood='Breakup', song_similarity='Edgy Love', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Freedom', song_mood='Revival', song_similarity='Dance', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Love Drought', song_mood='Breakup', song_similarity='Edgy Love', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Heaven', song_mood='Breakup', song_similarity='Love', song_genre='Pop', song_era='2010')
    Music(artist='Beyoncé', song_title='Blue', song_mood='Upbeat', song_similarity='Love', song_genre='Pop', song_era='2010')
    Music(artist='Blue Hawaii', song_title='Try to Be', song_mood='Upbeat', song_similarity='Dance', song_genre='Electronic', song_era='2010')
    Music(artist='Cee Lo Green', song_title='Fool For You', song_mood='Upbeat', song_similarity='Edgy Love', song_genre='Soul', song_era='2010')
    Music(artist='Casey James', song_title="Let's Don't Call It a Night", song_mood='Sexy', song_similarity='Love', song_genre='Country', song_era='2010')
    Music(artist='Cee Lo Green', song_title='Bright Lights Bigger City', song_mood='Upbeat', song_similarity='Dance', song_genre='Soul', song_era='2010')
    Music(artist='Cee Lo Green', song_title='Bodies', song_mood='Sexy', song_similarity='Edgy Love', song_genre='Soul', song_era='2010')
    Music(artist='Cee Lo Green', song_title='I Want You', song_mood='Upbeat', song_similarity='Dance', song_genre='Soul', song_era='2010')
    Music(artist='Cee Lo Green', song_title='Love Gun (feat. Lauren Bennett)', song_mood='Sexy', song_similarity='Edgy Love', song_genre='Soul', song_era='2010')
    Music(artist='Cee Lo Green', song_title='No One's Gonna Love You', song_mood='Dark', song_similarity='Edgy Love', song_genre='Soul', song_era='2010')
    Music(artist='Tupac Shakur', song_title='The Realist Killaz (feat. 50 Cent)', song_mood='Beatin', song_similarity='Edgy', song_genre='Hiop-Hop', song_era='2010')
    Music(artist='Natalie Imbruglia', song_title="Don't You Think", song_mood='Dark', song_similarity='Edgy', song_genre='Alternative Rock', song_era='1990')
    Music(artist='Macy Gray', song_title='A Moment To Myself', song_mood='Upbeat', song_similarity='Funky Love', song_genre='Soul', song_era='1990')
    Music(artist='Jay Z', song_title='On To The Next One (feat. Swizz Beatz)', song_mood='Beatin', song_similarity='Edgy', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Jean Grae', song_title='Uh Oh (feat. Talib Kwele', song_mood='Beatin', song_similarity='Edgy', song_genre='Hip-Hop', song_era='2010')
    Music(artist='Jean Grae', song_title="Don't Rush Me", song_mood='Beatin', song_similarity='Chill', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Jean Grae', song_title='Supa Luv', song_mood='Breakup', song_similarity='Edgy Love', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Smashing Pumpkins', song_title='Siva', song_mood='Screamy', song_similarity='Edgy', song_genre='Rock', song_era='2000')
    Music(artist='Tupac Shakur', song_title='Same Song', song_mood='Upbeat', song_similarity='Dance', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Vivian Green', song_title='Damn', song_mood='Breakup', song_similarity='Edgy Love', song_genre='Soul', song_era='2000')
    Music(artist='Wale', song_title='Bad (feat. Rihanna', song_mood='Sexy', song_similarity='Dance', song_genre='R&B', song_era='2010')
    Music(artist='Tata Vega', song_title='Maybe God's Trying To Tell You Something', song_mood='Revival', song_similarity='Dance', song_genre='Gospel', song_era='1980')
    Music(artist='Prince', song_title='Kiss', song_mood='Upbeat', song_similarity='Edgy Love', song_genre='Love', song_era='1980')
    Music(artist='Prince', song_title='Purple Rain', song_mood='Melancholy', song_similarity='Chill Love', song_genre='Rock', song_era='1980')
    Music(artist='Prince', song_title='Controversy', song_mood='Upbeat', song_similarity='Edgy', song_genre='Rock', song_era='1980')
    Music(artist='Stevie Wonder', song_title='Living For The City', song_mood='Upbeat', song_similarity='Dance', song_genre='Soul', song_era='1970')
    Music(artist='Minnie Ripperton', song_title='They Call It Stormy Monday', song_mood='Breakup', song_similarity='Dance', song_genre='Soul', song_era='1960')
    Music(artist='Minnie Ripperton', song_title='Respect', song_mood='Upbeat', song_similarity='Love', song_genre='Soul', song_era='1960')
    Music(artist='Sublime', song_title='Burritos', song_mood='Upbeat', song_similarity='Edgy', song_genre='Rock', song_era='1990')
    Music(artist='Stevie Wonder', song_title='Golden Lady', song_mood='Upbeat', song_similarity='Dance', song_genre='Soul', song_era='1970')
    Music(artist='A Tribe Called Quest', song_title='Bonita Applebaum', song_mood='Beatin', song_similarity='Edgy Love', song_genre='Hip-Hop', song_era='1990')
    Music(artist='A Tribe Called Quest', song_title='Can I Kick It', song_mood='Beatin', song_similarity='Chill', song_genre='Hip-Hop', song_era='1990')
    Music(artist='Sade', song_title='Never As Good As The First Time', song_mood='Upbeat', song_similarity='Damce', song_genre='Soul', song_era='1980')
    Music(artist='Transistor', song_title='Rub A Dub', song_mood='Upbeat', song_similarity='Dance', song_genre='Alternative Punk', song_era='1990')
    Music(artist='Sade', song_title='The Sweetest Taboo', song_mood='Sexy', song_similarity='Dance', song_genre='Soul', song_era='1990')
    Music(artist='Mint Condition', song_title='Caught My Eye', song_mood='Sexy', song_similarity='Dance', song_genre='Soul', song_era='2010')
    Music(artist='Teena Marie', song_title='The Rose N' Thorn', song_mood='Breakup', song_similarity='Chill', song_genre='R&B', song_era='2000')
    Music(artist='T.I.', song_title="Big Shit Poppin'", song_mood='Beatin', song_similarity='Dance', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Kwes.', song_title='In & Out The UK', song_mood='Upbeat', song_similarity='Edgy', song_genre='EDM', song_era='2010')
    Music(artist='Outkast', song_title='Peaches (feat. Sleepy Brown & Scar', song_mood='Beatin', song_similarity='Chill', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Outkast', song_title='Greatest Show On Earth (feat. Macy Gray)', song_mood='Beatin', song_similarity='Edgy', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Outkast', song_title='In Your Dreams (feat. Janelle Monáe, Killer Mike & Sleepy Brown)', song_mood='Beatin', song_similarity='Chill', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Outkast', song_title="Idlewild Blue (Don'tchu Worry 'Bout me)", song_mood='Upbeat', song_similarity='Funky', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Jana Kramer', song_title="I Won't Give Up", song_mood='Melancholy', song_similarity='Love', song_genre='Country', song_era='2010')
    Music(artist='Mos Def', song_title='Sun, Moon, Stars', song_mood='Beatin', song_similarity='Funk', song_genre='Hip-Hop', song_era='2000')
    Music(artist='Trey Songz', song_title='Gotta Go', song_mood='Breakup', song_similarity='Chill', song_genre='Soul', song_era='2000')
    Music(artist='Lustra', song_title="Scotty Doesn't Know", song_mood='Upbeat', song_similarity='Edgy Love', song_genre='Alternative Punk', song_era='2000')
  ]
  for music in data:
        db.session.add(music)
    db.session.commit()

def undo_musics():
    db.session.execute('TRUNCATE musics RESTART IDENTITY CASCADE;')
    db.session.commit()