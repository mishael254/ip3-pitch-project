from flask_login import UserMixin
from .import login_manager
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User (UserMixin,db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitches',backref = 'user',lazy = 'dynamic')
    comments = db.relationship('Comments',backref = 'user',lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)





    def __repr__(self):
        return f'User {self.username}'

class Pitches (db.Model):
    """ Pitches model """

    __tablename__ = "pitches"
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255),index = True)
    pitch = db.Column(db.String(255),unique = True,index = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comments',backref = 'pitch',lazy ='dynamic')



    def __repr__(self):
        return f'Pitches {self.pitch}'

class Comments (db.Model):
    """ Comments model """

    __tablename__ = "comments"
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255),index = True)
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
