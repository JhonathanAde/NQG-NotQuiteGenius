from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileAllowed
# from app.models import Song, Artist


# def user_exists(form, field):
#     print("Checking if user exits", field.data)
#     email = field.data
#     user = User.query.filter(User.email == email).first()
#     if user:
#         raise ValidationError("User is already registered.")


class SongForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    artist_id = IntegerField('Artist ID', validators=[DataRequired()])
    lyrics = TextAreaField('Lyrics', validators=[DataRequired()])
    image = FileField('Album art', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'jpg and png only!')])
    audio_file = FileField('Audio', validators=[FileAllowed(['mp3', 'wav'], 'mp3 or wav files only!')])
