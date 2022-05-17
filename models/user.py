#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user')
        reviews = relationship('Review', backref='user')
else:
    class User(BaseModel):
        """Model for users"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
