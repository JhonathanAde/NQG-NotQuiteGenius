from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileAllowed
# from app.models import Song, Artist

class ArtistForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField('Artist image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'jpg and png only!')])