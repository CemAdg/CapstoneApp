import os
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    #db.create_all()


"""
drops the database tables and starts fresh
can be used to initialize a clean database
"""
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Movies with attributes title and release date 
'''
class Movie(db.Model):  
  __tablename__ = 'Movies'

  id = Column(Integer, primary_key=True)
  title = Column(String, nullable=False)
  release_date = Column(Date, nullable=False)

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date


  """
  format()
    representation of Movie model
  """
  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date}


  """
   insert()
      inserts a new model into a database
  """
  def insert(self):
    db.session.add(self)
    db.session.commit() 


  """
  update()
      updates a new model into a database
      the model must exist in the database
  """
  def update(self):
    db.session.commit()


  """
  delete()
      deletes a new model into a database
      the model must exist in the database
  """
  def delete(self):
    db.session.delete(self)
    db.session.commit()



'''
Actors with attributes name, age and gender 
'''
class Actor(db.Model):  
  __tablename__ = 'Actors'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  age = Column(Integer, nullable=False)
  gender = Column(String, nullable=False)  

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender


  """
  format()
    representation of Actor model
  """
  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender}


  """
   insert()
      inserts a new model into a database
  """
  def insert(self):
    db.session.add(self)
    db.session.commit() 


  """
  update()
      updates a new model into a database
      the model must exist in the database
  """
  def update(self):
    db.session.commit()


  """
  delete()
      deletes a new model into a database
      the model must exist in the database
  """
  def delete(self):
    db.session.delete(self)
    db.session.commit()