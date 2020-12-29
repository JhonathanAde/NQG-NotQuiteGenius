from sqlalchemy.orm import relationship
from .db import db

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key = True)
    name  = db.Column(db.String(40), nullable = False)
    image  = db.Column(db.String(150), nullable = True)

    songs = relationship('Song', back_populates='artist', order_by='asc(Song.id)')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "songs": [song.to_dict() for song in self.songs]
        }

    def to_dict_no_songs(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
        }