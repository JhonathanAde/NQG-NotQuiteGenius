# from werkzeug.security import generate_password_hash
from app.models import db, Artist

# Adds a demo user, you can add other users here if you want
def seed_artists():

    taylor = Artist(
        name='Taylor Swift',
        image='https://nqg-images.s3.amazonaws.com/Taylor_Swift-01.png'
    )
    cudi = Artist(
        name='Kid Cudi',
        image='https://nqg-images.s3.amazonaws.com/Kid_Cudi-01.png'
    )
    weeknd = Artist(
        name='The Weeknd',
        image='https://nqg-images.s3.amazonaws.com/The_Weeknd-01.png'
    )
    halsey = Artist(
        name='Halsey',
        image='https://nqg-images.s3.amazonaws.com/Halsey-01.png'
    )
    billie = Artist(
        name='Billie Eilish',
        image='https://nqg-images.s3.amazonaws.com/Bilie_Eilish-01.png'
    )
    saint_jhn = Artist(
        name='SAINT JHN',
        image='https://nqg-images.s3.amazonaws.com/Saint_Jhn-01.png'
    )
    future = Artist(
        name='Future',
        image='https://nqg-images.s3.amazonaws.com/Future-01.png'
    )
    tame = Artist(
        name='Tame Impala',
        image='https://nqg-images.s3.amazonaws.com/Tame_Impala.png'
    )
    bob = Artist(
        name='Bob Dylan',
        image='https://nqg-images.s3.amazonaws.com/Bob_Dylan-01.png'
    )
    maren = Artist(
        name='Maren Morris',
        image='https://nqg-images.s3.amazonaws.com/Maren_Morris-01.png'
    )
    perfume = Artist(
        name='Perfume Genius',
        image='https://nqg-images.s3.amazonaws.com/Perfume_genius-01.png'
    )
    bad_bunny = Artist(
        name='Bad Bunny',
        image='https://nqg-images.s3.amazonaws.com/Bad_bunny-01.png'
    )
    fiona = Artist(
        name='Fiona Apple',
        image='https://nqg-images.s3.amazonaws.com/Fiona_Apple-01.png'
    )
    mac_miller = Artist(
        name='Mac Miller',
        image='https://nqg-images.s3.amazonaws.com/Mac_Miller-01.png'
    )
    selena_gomez = Artist(
        name='Selena Gomez',
        image='https://nqg-images.s3.amazonaws.com/Salena_Gomez-01.png'
    )
    benee = Artist(
        name='BENEE',
        image='https://nqg-images.s3.amazonaws.com/Benee-01.png'
    )
    the_chicks = Artist(
        name='The Chicks',
        image='https://nqg-images.s3.amazonaws.com/The_Chicks01.png'
    )
    grimes = Artist(
        name='Grimes',
        image='https://nqg-images.s3.amazonaws.com/Grimes-01.png'
    )
    dua_lipa = Artist(
        name='Dua Lipa',
        image='https://nqg-images.s3.amazonaws.com/Dua_Lipa-01.png'
    )
    lady_gaga = Artist(
        name='Lady Gaga',
        image='https://nqg-images.s3.amazonaws.com/Lady_gaga-01.png'
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