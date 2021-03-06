from sqlalchemy.orm import relationship
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
