# from werkzeug.security import generate_password_hash
from app.models import db, Artist

# Adds a demo user, you can add other users here if you want
def seed_artists():

    taylor = Artist(
        name='Taylor Swift',
        image=''
    )
    cudi = Artist(
        name='Kid Cudi',
        image=''
    )
    weeknd = Artist(
        name='The Weeknd',
        image=''
    )
    halsey = Artist(
        name='Halsey',
        image=''
    )
    billie = Artist(
        name='Billie Eilish',
        image=''
    )
    saint_jhn = Artist(
        name='SAINT JHN',
        image=''
    )
    future = Artist(
        name='Future',
        image=''
    )
    tame = Artist(
        name='Tame Impala',
        image=''
    )
    bob = Artist(
        name='Bob Dylan',
        image=''
    )
    maren = Artist(
        name='Maren Morris',
        image=''
    )
    perfume = Artist(
        name='Perfume Genius',
        image=''
    )
    bad_bunny = Artist(
        name='Bad Bunny',
        image=''
    )
    fiona = Artist(
        name='Fiona Apple',
        image=''
    )
    mac_miller = Artist(
        name='Mac Miller',
        image=''
    )
    selena_gomez = Artist(
        name='Selena Gomez',
        image=''
    )
    benee = Artist(
        name='BENEE',
        image=''
    )
    the_chicks = Artist(
        name='The Chicks',
        image=''
    )
    grimes = Artist(
        name='Grimes',
        image=''
    )
    dua_lipa = Artist(
        name='Dua Lipa',
        image=''
    )
    lady_gaga = Artist(
        name='Lady Gaga',
        image=''
    )


    db.session.add(taylor)
    db.session.add(cudi)
    db.session.add(weeknd)
    db.session.add(halsey)
    db.session.add(billie)
    db.session.add(saint_jhn)
    db.session.add(future)
    db.session.add(tame)
    db.session.add(bob)
    db.session.add(maren)
    db.session.add(perfume)
    db.session.add(bad_bunny)
    db.session.add(fiona)
    db.session.add(mac_miller)
    db.session.add(selena_gomez)
    db.session.add(benee)
    db.session.add(the_chicks)
    db.session.add(grimes)
    db.session.add(dua_lipa)
    db.session.add(lady_gaga)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_artists():
    db.session.execute('TRUNCATE artists;')
    db.session.commit()