from flask import Blueprint, jsonify, request
# from flask_login import login_required
from app.models import Artist, Song, db
from app.forms import SongForm

song_routes = Blueprint('songs', __name__)

# GETS ALL SONGS
@song_routes.route('/', methods=["GET"])
def get_songs():
    songs = Song.query.all()
    print("songs", songs)
    return {"songs": [song.to_dict() for song in songs]}


# CREATE SONG
@song_routes.route('/', methods=["POST"])
def create_song():
    print("INSIDE CREATE SONG!!")
    form = SongForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Check for existing artist
        # artist = Artist.query.filter(Artist.name === form.data['name']).first()

        # artist = Artist(
        #     name=form.data['name'],
        #     image=form.data['image']
        # )

        # db.session.add(artist)
        # db.session.commit()

        # getArtist = Artist.query.filter()

        # song = Song(
        #     title=form.data['title'],
        #     artist_id
        #     lyrics
        #     image
        #     audio_files
        # )
        # return user.to_dict()
        # img = request.files['image']

        # img = form.data
        img = form.image.data
        print(f"IMAGE: {img}")

        print('HERE!')
        return {"result": "SUCCESS!"}
    else:
        print(f"FORM ERRORS: {form.errors}")
        return {"result": "FAILED!"}


    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# GETS ONE SONG
@song_routes.route('/<int:id>', methods=["GET"])
def get_one_song(id):
    song = Song.query.get(id)
    return song.to_dict()



# import boto3
# from botocore.client import Config

# ACCESS_KEY_ID = ''
# ACCESS_SECRET_KEY = ''
# BUCKET_NAME = 'img-bucket-00123'

# data = open('bitmoji.png', 'rb')

# s3 = boto3.resource(
#     's3',
#     aws_access_key_id=ACCESS_KEY_ID,
#     aws_secret_access_key=ACCESS_SECRET_KEY,
#     config=Config(signature_version='s3v4')
# )
# s3.Bucket(BUCKET_NAME).put_object(Key='bitmoji.png', Body=data)

# print ("Done")