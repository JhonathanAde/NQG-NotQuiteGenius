import re
from app.models import Annotation, Song, Artist, User, db
from flask import Blueprint, request
from sqlalchemy import or_

search_routes = Blueprint('search', __name__)

# TEXT SEARCH OF DATABASE
@search_routes.route('/')
def search_database():
    search_string = request.args.get('search_string')

    # Get exact match strings
    exact_strings = re.findall('"([^"]*)"', search_string)
    exact_strings = list(set(exact_strings))

    words = search_string

    if (words):
        for phrase in exact_strings:
            pattern = re.compile(f'"{phrase}"')
            words = re.sub(pattern, "", words)
            #Check that exact word is a whole word
            #If so, check to remove it from words
            if (len(phrase.split()) == 1):
                words = re.sub(phrase, "", words)

    words = list(set(words.split()))

    if (exact_strings or words):
        return search(exact_strings, words)
    else:
        return {"error": "Missing search string from request."}

#Helper function
def search(exacts, words):

    lyrics = db.session.query(Song). \
        filter(or_(*[Song.lyrics.ilike(f'%{pattern}%') for pattern in words])).all()
    titles = db.session.query(Song). \
        filter(or_(*[Song.title.ilike(f'%{pattern}%') for pattern in words])).all()
    artists = db.session.query(Artist). \
        filter(or_(*[Artist.name.ilike(f'%{pattern}%') for pattern in words])).all()
    annotations = db.session.query(Annotation). \
        filter(or_(*[Annotation.content.ilike(f'%{pattern}%') for pattern in words])).all()


    return {
        "titles": [song.to_dict() for song in titles],
        "lyrics": [song.to_dict() for song in lyrics],
        "artists": [artist.to_dict() for artist in artists],
        "annotations": [annot.to_dict() for annot in annotations],
        }


# def vector_search(cls, search_string, dictionary='english'):
#     lyrics = db.session.query(cls). \
#         filter(func.to_tsvector(dictionary, getattr(cls, 'lyrics')).match(search_string, postgresql_regconfig='english')).all()
#     titles = db.session.query(cls). \
#         filter(func.to_tsvector(dictionary, getattr(cls, 'title')).match(search_string, postgresql_regconfig='english')).all()
#     # artist = db.session.query(cls). \
#     #     filter(func.to_tsvector('english', getattr(cls, 'title')).match(search_string, postgresql_regconfig='english')).all()


#     return {
#         "titles": [song.to_dict() for song in titles],
#         "lyrics": [song.to_dict() for song in lyrics]
#         }
