from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class AnnotationForm(FlaskForm):
  user_id = IntegerField('user_id', validators=[DataRequired()])
  song_id = IntegerField('song_id', validators=[DataRequired()])
  lyric_key = StringField('lyric_key', validators=[DataRequired()])
  content = TextAreaField('Content', validators=[DataRequired()])

