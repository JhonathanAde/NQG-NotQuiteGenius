from sqlalchemy.orm import relationship
from .db import db

class Annotation(db.Model):
    __tablename__ = 'annotations'

    id = db.Column(db.Integer, primary_key = True)
    user_id  = db.Column(db.ForeignKey('users.id'))
    song_id =  db.Column(db.ForeignKey('songs.id'))
    lyric_key = db.Column(db.String(150), nullable = False)
    content = db.Column(db.String(500), nullable = False)

    song = relationship('Song', back_populates="annotations")
    user = relationship('User', back_populates="annotations")
    # artist = relationship('Artist', back_populates='songs')


    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "songId": self.song_id,
            "lyricKey": self.lyric_key,
            "content": self.content,
            "song": self.song,
            "user": self.user
        }
    