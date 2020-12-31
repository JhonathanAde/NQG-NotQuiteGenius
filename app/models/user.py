from sqlalchemy.orm import relationship
from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False, unique = True)
    is_admin = db.Column(db.Boolean, nullable = False, default = False)
    email = db.Column(db.String(255), nullable = False, unique = True)
    hashed_password = db.Column(db.String(255), nullable = False)

    annotations = relationship('Annotation', back_populates='user', order_by='asc(Annotation.id)')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    def to_dict(self):
        return {
        "id": self.id,
        "username": self.username,
        "email": self.email,
        "isAdmin": self.is_admin,
        }
    
    # def annotations(self):
    #     return [annotation.to_dict() for annotation in self.annotations]
