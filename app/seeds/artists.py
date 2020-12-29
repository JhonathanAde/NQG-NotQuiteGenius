# from werkzeug.security import generate_password_hash
from app.models import db, Artist

# Adds a demo user, you can add other users here if you want
def seed_artists():

    taylor = Artist(name='Taylor Swift')
    cudi = Artist(name='Kid Cudi')
    weeknd = Artist(name='The Weeknd')

    db.session.add(taylor)
    db.session.add(cudi)
    db.session.add(weeknd)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_artists():
    db.session.execute('TRUNCATE artists;')
    db.session.commit()