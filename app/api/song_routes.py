from flask import Blueprint, jsonify, request, url_for
import boto3
import mimetypes
from werkzeug.utils import secure_filename
# from flask_login import login_required
from app.models import Song, Annotation, db
from app.forms import SongForm, AnnotationForm


song_routes = Blueprint('songs', __name__)

# REGEX TO CHECK FOR EXTENSIONS
#  \.(?i)(jpe?g|png|gif)$

def validation_errors_to_error_messages(validation_errors):
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

    img = ''
    img_path = ''
    if form.validate_on_submit():
        if request.files:
            # image file
            img = request.files['image']
            img_name = secure_filename(img.filename)

            # song file
            song = request.files['audio_file']
            song_name = secure_filename(song.filename)

            mime_type = mimetypes.guess_type(img_name)
            song_mime_type = mimetypes.guess_type(song_name)
            print(f"MIME TYPE FOR UPLOADED FILE!!! {mime_type}")

            s3 = boto3.resource('s3')
            uploaded_image = s3.Bucket('nqg-images').put_object(Key=img_name, Body=img, ACL='public-read', ContentType=mime_type[0])

            uploaded_song = s3.Bucket('nqg-songs').put_object(Key=song_name, Body=song, ACL='public-read', ContentType=song_mime_type[0])

            img_path = f"https://nqg-images.s3.amazonaws.com/{img_name}"
            song_path = f"https://nqg-songs.s3.amazonaws.com/{song_name}"
        else:
            print("SOME FILES WEREN'T SENT!")


        song = Song(
            title=form.data['title'],
            artist_id=form.data['artist_id'],
            lyrics=form.data['lyrics'],
            image=img_path,
            audio_file=song_path
        )

        db.session.add(song)
        db.session.commit()
        return song.to_dict()
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# GETS ONE SONG
@song_routes.route('/<int:id>', methods=["GET"])
def get_one_song(id):
    song = Song.query.get(id)
    return song.to_dict()


# EDIT SONG
@song_routes.route('/<int:id>', methods=["PATCH"])
def edit_song(id):
    form = SongForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    img = ''
    img_path = ''
    if form.validate_on_submit():
        if request.files:
            # image file 
            img = request.files['image']
            img_name = secure_filename(img.filename)

             # song file
            song = request.files['audio_file']
            song_name = secure_filename(song.filename)

            mime_type = mimetypes.guess_type(img_name)
            song_mime_type = mimetypes.guess_type(song_name)

            s3 = boto3.resource('s3')
            uploaded_image = s3.Bucket('nqg-images').put_object(Key=img_name, Body=img, ACL='public-read', ContentType=mime_type[0])
            uploaded_song = s3.Bucket('nqg-songs').put_object(Key=song_name, Body=song, ACL='public-read', ContentType=song_mime_type[0])

            img_path = f"https://nqg-images.s3.amazonaws.com/{img_name}"
            song_path = f"https://nqg-songs.s3.amazonaws.com/{song_name}"
        else:
            print("NO IMAGE WAS SENT!")

        song_to_edit = Song.query.get(id)
        # if !song:
        #     return {"error":f"song with song ID {id} does not exist."}

        song_to_edit.title = form.data['title']
        song_to_edit.artist_id = form.data['artist_id']
        song_to_edit.lyrics = form.data['lyrics']
        song_to_edit.image = img_path
        song_to_edit.audio_file = song_path

        db.session.add(song_to_edit)
        db.session.commit()

        return song_to_edit.to_dict()
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# DELETE SONG
@song_routes.route('/<int:id>', methods=["DELETE"])
def delete_song(id):
    song_to_delete = Song.query.get(id)
    if song_to_delete:
        song_to_delete.delete()
        return {"response": f"Song with ID {id} has been deleted."}
    else:
        return {"errors": [f"Song with ID {id} does not exist."]}

# GETS AN ANNOTATION
@song_routes.route('/annotations/<int:id>', methods=["GET"])
def get_annotations(id):
    annotations = Annotation.query.filter_by(user_id = id)
    print("annotations", annotations)
    return [annotation.to_dict() for annotation in annotations]

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
        return annotation.to_dict()
    else:
        return {"error": True}

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
