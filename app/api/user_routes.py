from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Annotation, Song, Artist
from sqlalchemy.orm import joinedload

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

# GETS AN ANNOTATION
@user_routes.route('/<int:id>/annotations', methods=["GET"])
def get_annotations(id):
    annotations = Annotation.query.filter_by(user_id = id)
    # annotations = Annotation.query.options(joinedload("song"))
    print("annotations!!!!", [annotation.to_dict() for annotation in annotations])
    return {"annotations": [annotation.to_dict() for annotation in annotations]}