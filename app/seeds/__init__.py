from app import models
from flask.cli import AppGroup
from .users import seed_users, undo_users
from .artists import seed_artists, undo_artists
from .songs import seed_songs, undo_songs
from .annotations import seed_annotations, undo_annotations
from app.models import Song, db

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_artists()
    seed_songs()
    seed_annotations()

    #set the search vectors for Songs
    # songs = Song.query.all()
    # for song in songs:
    #     song.create_tsvector()

    # db.session.bulk_save_objects(songs)
    # db.session.commit()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_artists()
    undo_songs()
    undo_annotations()
    # Add other undo functions here
