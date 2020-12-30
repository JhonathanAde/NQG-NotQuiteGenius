import os
from flask import Blueprint, jsonify, request, url_for
import boto3
from werkzeug.utils import secure_filename
# from flask_login import login_required
from app.models import Artist, Song, Annotation, db
from app.forms import SongForm, AnnotationForm


song_routes = Blueprint('songs', __name__)
UPLOAD_FOLDER = '../uploads/images/'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# GETS ALL SONGS
@song_routes.route('/', methods=["GET"])
def get_songs():
    songs = Song.query.all()
    print("songs", songs)
    return {"songs": [song.to_dict() for song in songs]}


# CREATE SONG
@song_routes.route('/', methods=["POST"])
def create_song():
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

        img = request.files['image']
        img_name = secure_filename(img.filename)
        print(f"FILE NAME!! {img_name}")

        s3 = boto3.resource('s3')
        result = s3.Bucket('nqg-images').put_object(Key=img_name, Body=img)

        img_path = f"https://nqg-images.s3.amazonaws.com/{img_name}"
        print(f"IMG PATH!! {img_path}")

        song = Song(
            title=form.data['title'],
            artist_id=form.data['artist_id']
            lyrics
            image
            audio_files
        )
        return user.to_dict()

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



# POSTS AN ANNOTATION
@song_routes.route('/<int:id>/annotations', methods=["POST"])
def post_annotation(id):
    form = AnnotationForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        annotation = Annotation(
            user_id=form.data['user_id'],
            song_id=id,
            lyric_key=form.data['lyric_key'],
            content=form.data['content']
        )
        db.session.add(annotation)
        db.session.commit()
        return "Sucess!!"
    else:
        return "Why bro?"

# UPDATES AN ANNOTATION
@song_routes.route('/annotations/<int:id>', methods=["GET", "POST"])
def update_annotation(id):
    annotation = Annotation.query.filter_by(id=id).first()
    if request.method == 'POST':
        if annotation:
            db.session.delete(annotation)
            db.session.commit()

            form = AnnotationForm()
            form['csrf_token'].data = request.cookies['csrf_token']
            if form.validate_on_submit():
                annotation = Annotation(
                    user_id=form.data['user_id'],
                    song_id=form.data['song_id'],
                    lyric_key=form.data['lyric_key'],
                    content=form.data['content']
                )
                db.session.add(annotation)
                db.session.commit()
     







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