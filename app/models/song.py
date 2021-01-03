from app.models import annotation
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func
# from sqlalchemy.dialects.postgresql import TSVECTOR
from .db import db

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    artist_id = db.Column(db.ForeignKey('artists.id'))
    lyrics = db.Column(db.Text, nullable = False)
    image = db.Column(db.String(150), nullable = True)
    audio_file = db.Column(db.String(150), nullable = True)

    artist = relationship('Artist', back_populates='songs')
    annotations = relationship('Annotation', back_populates='song', order_by='asc(Annotation.id)')

    def to_dict(self):
        return {
            "id": self.id,
            "artistId": self.artist_id,
            "title": self.title,
            "lyrics": self.lyrics,
            "image": self.image,
            "audioFile": self.audio_file,
            "artist": self.artist.to_dict_no_songs(),
            "annotations": [annotation.to_dict() for annotation in self.annotations],
        }

    def to_dict_no_anno(self):
        return {
            "id": self.id,
            "artistId": self.artist_id,
            "title": self.title,
            "lyrics": self.lyrics,
            "image": self.image,
            "audioFile": self.audio_file,
            "artist": self.artist.to_dict_no_songs(),
        }

    @classmethod
    def vector_search(cls, search_string, dictionary='english'):
        lyrics = db.session.query(cls). \
            filter(func.to_tsvector(dictionary, getattr(cls, 'lyrics')).match(search_string, postgresql_regconfig='english')).all()
        titles = db.session.query(cls). \
            filter(func.to_tsvector(dictionary, getattr(cls, 'title')).match(search_string, postgresql_regconfig='english')).all()
        # artist = db.session.query(cls). \
        #     filter(func.to_tsvector('english', getattr(cls, 'title')).match(search_string, postgresql_regconfig='english')).all()


        return {
            "titles": [song.to_dict() for song in titles],
            "lyrics": [song.to_dict() for song in lyrics]
            }

    @classmethod
    def search(cls, search_string):
        stripped_of_html_lyrics = getattr(cls, 'lyrics').replace('<br />', ' ')
        lyrics = db.session.query(cls). \
            filter(getattr(cls, 'lyrics').ilike(f'%{search_string}%')).all()
        titles = db.session.query(cls). \
            filter(getattr(cls, 'title').ilike(f'%{search_string}%')).all()
        # artist = db.session.query(cls). \
        #     filter(func.to_tsvector('english', getattr(cls, 'title')).match(search_string, postgresql_regconfig='english')).all()


        return {
            "titles": [song.to_dict() for song in titles],
            "lyrics": [song.to_dict() for song in lyrics]
            }

    # def create_tsvector(self):
    #     print()
    #     song = self.to_dict()
    #     annotation_content = [annotation["content"] for annotation in song["annotations"]]

    #     search_array = [
    #         song["lyrics"].replace('<br />',' '),
    #         song["title"],
    #         song["artist"]["name"],
    #     ] + annotation_content

    #     vector = func.to_tsvector("english", " ".join(search_array))
    #     print("VVVVVVVV", vector[0])
    #     self._search_ = vector
