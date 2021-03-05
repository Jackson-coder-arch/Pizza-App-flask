from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    order = db.relationship('Order',backref = 'user',lazy="dynamic")
    # comments = db.relationship('Comment',backref = 'user',lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    def save_user(self):
        db.session.add(self)
        db.session.commit()



    def __repr__(self):
        return f'User {self.username}'

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer,primary_key = True)
    title =  db.Column(db.String(255)) 
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    # comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    

    def __repr__(self):
        return f'User {self.description}'
