from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, ValidationError
# from app.models import Song, Artist


# def user_exists(form, field):
#     print("Checking if user exits", field.data)
#     email = field.data
#     user = User.query.filter(User.email == email).first()
#     if user:
#         raise ValidationError("User is already registered.")


class SongForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    lyrics = TextAreaField('lyrics', validators=[DataRequired()])
    image = FileField('Album art')
