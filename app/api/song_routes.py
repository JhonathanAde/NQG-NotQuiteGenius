import os
from flask import Blueprint, jsonify, request, url_for
import boto3
from werkzeug.utils import secure_filename
# from flask_login import login_required
from app.models import Artist, Song, Annotation, db
from app.forms import SongForm, AnnotationForm


song_routes = Blueprint('songs', __name__)
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


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
        img = request.files['image']
        img_name = secure_filename(img.filename)
        print(f"FILE NAME!! {img_name}")

        s3 = boto3.resource('s3')
        result = s3.Bucket('nqg-images').put_object(Key=img_name, Body=img)

        img_path = f"https://nqg-images.s3.amazonaws.com/{img_name}"
        print(f"IMG PATH!! {img_path}")

        # song = Song(
        #     title=form.data['title'],
        #     artist_id=form.data['artist_id']
        #     lyrics
        #     image
        #     audio_files
        # )
        # return song.to_dict()
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401


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
        print("#######", annotation)
        db.session.add(annotation)
        db.session.commit()
        return "Sucess!"
    else:
        return "Form was not validated"

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
     
