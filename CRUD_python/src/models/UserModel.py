from marshmallow import fields, Schema
import datetime
from . import db

class UserModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  isbn = db.Column(db.String(128), nullable=False)
  authors = db.Column(db.String(128), nullable=True)
  country = db.Column(db.String(128), nullable=True)
  pages = db.Column(db.String(128), nullable=True)
  publisher = db.Column(db.String(128), nullable=True)
  release_date = db.Column(db.String(128), nullable=True)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.id = data.get("id")
    self.name = data.get('name')
    self.isbn = data.get('isbn')
    self.authors = data.get('authors')
    self.country = data.get('country')
    self.pages = data.get('pages')
    self.publisher = data.get('publisher')
    self.release_date = data.get('release_date')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_users():
    return UserModel.query.all()

  @staticmethod
  def get_one_user(id):
    return UserModel.query.get(id)

  
  def __repr(self):
    return '<id {}>'.format(self.id)

  # add this class
class UserSchema(Schema):
  """
  User Schema
  """
  id = fields.Int(required=True)
  name = fields.Str(required=True)
  isbn = fields.Str(required=True)
  authors = fields.Str(required=True)
  country = fields.Str(required=True)
  pages = fields.Str(required=True)
  publisher = fields.Str(required=True)
  release_date = fields.Str(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
  
