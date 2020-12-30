import os
from flask import Blueprint, jsonify, request
import boto3
import mimetypes
from werkzeug.utils import secure_filename
from app.models import Artist, db
from app.forms import ArtistForm

artist_routes = Blueprint('artists', __name__)

def validation_errors_to_error_messages(validation_errors):
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages

# GETS ALL ARTISTS
@artist_routes.route('/', methods=["GET"])
def all_artist():
    artists = Artist.query.all()
    return {"artists": [artist.to_dict() for artist in artists]}

# CREATE ARTIST
@artist_routes.route('/', methods=["POST"])
def artist():
    form = ArtistForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    img = ''
    img_path = ''
    if form.validate_on_submit():
        if request.files:
            img = request.files['image']
            print(f"CHECK TO SEE IF IMG EXISTS: {img}")
            img_name = secure_filename(img.filename)
            # print(f"FILE NAME!! {img_name}")

            mime_type = mimetypes.guess_type(img_name)
            print(f"MIME TYPE FOR UPLOADED FILE!!! {mime_type}")
            
            s3 = boto3.resource('s3')
            uploaded_image = s3.Bucket('nqg-images').put_object(Key=img_name, Body=img, ACL='public-read', ContentType=mime_type[0])

            img_path = f"https://nqg-images.s3.amazonaws.com/{img_name}"
        else:
            print("NO IMAGE WAS SENT!")

        artist = Artist(
                name=form.data['name'],
                image=img_path,
            )
        db.session.add(artist)
        db.session.commit()
        return artist.to_dict_no_songs()
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# GETS ONE ARTIST
@artist_routes.route('/<int:id>', methods=["GET"])
def one_artist(id):
    artist = Artist.query.get(id)
    return artist.to_dict()

# EDIT ARTIST
@artist_routes.route('/<int:id>', methods=["PATCH"])
def edit_artist(id):
    form = ArtistForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    img = ''
    img_path = ''
    if form.validate_on_submit():
        if request.files:
            img = request.files['image']
            print(f"CHECK TO SEE IF IMG EXISTS: {img}")
            img_name = secure_filename(img.filename)
            # print(f"FILE NAME!! {img_name}")

            mime_type = mimetypes.guess_type(img_name)
            print(f"MIME TYPE FOR UPLOADED FILE!!! {mime_type}")
            
            s3 = boto3.resource('s3')
            uploaded_image = s3.Bucket('nqg-images').put_object(Key=img_name, Body=img, ACL='public-read', ContentType=mime_type[0])

            img_path = f"https://nqg-images.s3.amazonaws.com/{img_name}"
        else:
            print("NO IMAGE WAS SENT!")
 
        artist_to_edit = Artist.query.get(id)
        # if !artist:
        #     return {"error":f"artist with ID {id} does not exist."}

        artist_to_edit.name = form.data['name']
        artist_to_edit.image = img_path

        db.session.add(artist_to_edit)
        db.session.commit()

        return artist_to_edit.to_dict()
    else:
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401
