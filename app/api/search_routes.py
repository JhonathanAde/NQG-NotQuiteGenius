import re
from app.models import Annotation, Song, Artist, User, db
from flask import Blueprint, request
from sqlalchemy import or_, and_
from collections import Counter, OrderedDict

search_routes = Blueprint('search', __name__)

# TEXT SEARCH OF DATABASE
@search_routes.route('/')
def search_database():
    search_string = request.args.get('search_string')

    # Get exact match strings
    exacts = re.findall('"([^"]*)"', search_string)
    exacts = list(set(exacts))

    words = search_string

    if (words):
        for phrase in exacts:
            pattern = re.compile(f'"{phrase}"')
            words = re.sub(pattern, "", words)
            #Check that exact word is a whole word
            #If so, check to remove it from words
            if (len(phrase.split()) == 1):
                words = re.sub(phrase, "", words)

    words = list(set(words.split()))

    if (exacts or words):
        return search(exacts, words)
    else:
        return {"error": "Missing search string from request."}

#Helper function
def search(exacts, words):
    # AND searches
    full_lyrics = db.session.query(Song). \
        filter(and_(*[Song.lyrics.like(f'%{pattern}%') for pattern in exacts], *[Song.lyrics.ilike(f'%{pattern}%') for pattern in words])).all()
    full_titles = db.session.query(Song). \
        filter(and_(*[Song.title.like(f'%{pattern}%') for pattern in exacts], *[Song.title.ilike(f'%{pattern}%') for pattern in words])).all()
    full_artists = db.session.query(Artist). \
        filter(and_(*[Artist.name.like(f'%{pattern}%') for pattern in exacts], *[Artist.name.ilike(f'%{pattern}%') for pattern in words])).all()
    full_annotations = db.session.query(Annotation). \
        filter(and_(*[Annotation.content.like(f'%{pattern}%') for pattern in exacts], *[Annotation.content.ilike(f'%{pattern}%') for pattern in words])).all()

    # OR searches
    lyrics = db.session.query(Song). \
        filter(or_(*[Song.lyrics.like(f'%{pattern}%') for pattern in exacts], *[Song.lyrics.ilike(f'%{pattern}%') for pattern in words])).all()
    titles = db.session.query(Song). \
        filter(or_(*[Song.title.like(f'%{pattern}%') for pattern in exacts], *[Song.title.ilike(f'%{pattern}%') for pattern in words])).all()
    artists = db.session.query(Artist). \
        filter(or_(*[Artist.name.like(f'%{pattern}%') for pattern in exacts], *[Artist.name.ilike(f'%{pattern}%') for pattern in words])).all()
    annotations = db.session.query(Annotation). \
        filter(or_(*[Annotation.content.like(f'%{pattern}%') for pattern in exacts], *[Annotation.content.ilike(f'%{pattern}%') for pattern in words])).all()

    #NOTE: any "full" hits must be added after non-full (OR) hits for proper weighting of duplicate hits after they are made unique
    raw_order_and_sanitized_songs = (
          [{"key": f"song_{song.id}", "type": "title", "object": song.to_dict(), "full": False} for song in titles] \
        + [{"key": f"song_{song.id}", "type": "lyric", "object": song.to_dict(), "full": False} for song in lyrics] \
        + [{"key": f"song_{song.id}", "type": "title", "object": song.to_dict(), "full": True} for song in full_titles] \
        + [{"key": f"song_{song.id}", "type": "lyric", "object": song.to_dict(), "full": True} for song in full_lyrics] \

    )

    raw_order_and_sanitized_annotations = (
          [{"key": f"annot_{annot.id}", "type": "annotation", "object": annot.to_dict(), "full": False} for annot in annotations] \
        + [{"key": f"annot_{annot.id}", "type": "annotation", "object": annot.to_dict(), "full": True} for annot in full_annotations]
    )

    raw_order_and_sanitized_artists = (
          [{"key": f"artist_{artist.id}", "type": "artist", "object": artist.to_dict(), "full": True} for artist in full_artists] \
        + [{"key": f"artist_{artist.id}", "type": "artist", "object": artist.to_dict(), "full": False} for artist in artists]
    )


    #Make unique listings by casting to a dictionary with keys to be unique
    unique_songs = list({song['key']: song for song in raw_order_and_sanitized_songs}.values())
    unique_annotations = list({a['key']: a for a in raw_order_and_sanitized_songs}.values())
    unique_artists = list({artist['key']: artist for artist in raw_order_and_sanitized_artists}.values())

    # Merge or Morph annotations into song objects
    for annot in unique_annotations:
        song_obj = annot["object"]["song"]
        song_id = song_obj["id"]
        song_key = f"song_{song_id}"
        if (song_key) in unique_songs: #Merge



    # Weight and order song results
    full_patterns = exacts + words



    for song in unique_songs:
        # Full search hit on all words gets 1000 weight to start
        profile = {
            "title": {"whole_weight": 0, "part_weight": 0, "total_weight": 0},
            "lyrics": {"whole_weight": 0, "part_weight": 0, "total_weight": 0},
            "annotations": {"whole_weight": 0, "part_weight": 0, "total_weight": 0},
            }
        locations = []

        for pattern in full_patterns:
            whole = rf"(?i)\b{pattern}\b"
            whole_exact = rf"\b{pattern}\b"
            part = rf"(?i)\B{pattern}\B | (?i)\B{pattern}\b | (?i)\b{pattern}\B"
            part_exact = rf"\B{pattern}\B | \B{pattern}\b | \b{pattern}\B"
            #Exact matches will double weight for that pattern
            #Whole will double weight
            #Titles get triple final weight
            content = ''
            if (song["type"] == "annotation"):
                content = song["object"]["content"]

            if (song["type"] == "title" or song["type"] == "lyric"):
                title = song["object"]["title"]
                lyrics = song["object"]["lyrics"]
                id = song["object"]["id"]
                display = title

                profile["title"]["whole_weight"] += (len(re.findall(whole, title)) * 2) + (len(re.findall(whole_exact, title)) * 2)
                profile["title"]["part_weight"] += len(re.findall(part, title))  + len(re.findall(part_exact, title))
                profile["title"]["total_weight"] += (profile["title"]["whole_weight"] + profile["title"]["part_weight"]) * 3

                profile["lyrics"]["whole_weight"] += (len(re.findall(whole, lyrics)) * 2) + (len(re.findall(whole_exact, lyrics)) * 2)
                profile["lyrics"]["part_weight"] += len(re.findall(part, lyrics))  + len(re.findall(part_exact, lyrics))
                profile["lyrics"]["total_weight"] += profile["lyrics"]["whole_weight"] + profile["lyrics"]["part_weight"]

            else: #The "song" is actually an annotation object
                annotation = song["object"]["content"]
                id = song["object"]["songId"]
                display = song["object"]["song"]["title"]

                profile["annotations"]["whole_weight"] += (len(re.findall(whole, annotation)) * 2) + (len(re.findall(whole_exact, annotation)) * 2)
                profile["annotations"]["part_weight"] += len(re.findall(part, annotation))  + len(re.findall(part_exact, annotation))
                profile["annotations"]["total_weight"] += profile["annotations"]["whole_weight"] + profile["annotations"]["part_weight"]


            if (profile["title"]["total_weight"]):
                locations += ["title"]
            if (profile["lyrics"]["total_weight"]):
                locations += ["lyrics"]
            if (profile["annotations"]["total_weight"]):
                locations += ["lyric annotation"]

            song["url"] = f"/songs/{id}"
            song["display"] = display
            song["locations"] = " & ".join(locations)

        song["weight"] = (1000 if song["full"] else 0) + (
            profile["title"]["total_weight"] +
            profile["lyrics"]["total_weight"] +
            profile["annotations"]["total_weight"]
        )

    # Roughly weight and add urls for Artists
    for artist in unique_artists:
        artist["url"] = f"/artists/{artist['object']['id']}"
        artist["weight"] = 2000 if artist["full"] else 1
        artist["display"] = artist['object']['name']
        artist["locations"] = "artist name"

    final_results = sorted(unique_songs + unique_artists, key=lambda item: item["weight"], reverse=True)

    return {"results": final_results}





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
