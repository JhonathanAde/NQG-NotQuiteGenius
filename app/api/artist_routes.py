from flask import Blueprint, jsonify
# from flask_login import login_required
from app.models import Artist

artist_routes = Blueprint('artists', __name__)

# GETS ALL ARTISTS
@artist_routes.route('/', methods=["GET"])
def all_artist():
    artists = Artist.query.all()
    return {"artists": [artist.to_dict() for artist in artists]}

# # CREATE ARTIST
# @artist_routes.route('/', methods=["POST"])
# def artist(id):
#     artist = Artist.query.get(id)
#     return artist.to_dict()

# GETS ONE ARTIST
@artist_routes.route('/<int:id>', methods=["GET"])
def one_artist(id):
    artist = Artist.query.get(id)
    return artist.to_dict()
