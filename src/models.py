import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Aquí definimos las columnas de la tabla 'user'.
    # Ten en cuenta que cada columna es también un atributo de instancia de Python normal.
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    comments = Column(String(250), nullable=False)
    comments_like = Column(String(250), nullable=False)
    post_like = Column(String(250), nullable=False)
    posts = relationship("Post", backref="user")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date_published = Column(String(250), nullable=False)
    latitude = Column(String(250), nullable=True)
    longitud = Column(String(250), nullable=True)
    tags = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=False)
    content = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    comment = relationship("Comment", backref="post")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    date_published = Column(String(250), nullable=False)
    comment_likes = Column(Integer, nullable=False)
    content = Column(String(250), nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)   
    post_id = Column(Integer, ForeignKey('post.id')) 
    post = relationship(Post)  

class Like(Base):
    __tablename__ = 'like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)   
    post_id = Column(Integer, ForeignKey('post.id')) 
    post = relationship(Post) 

class CommentLike(Base):
    __tablename__ = 'comment_like'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship(User)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comments = relationship(Comment)      

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
