#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.base_model import BaseModel, Base
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Review(BaseModel, Base):
        """ Review classto store review information """
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey(
            'places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey(
            'users.id'), nullable=False)
else:
    class Review(BaseModel):
        """Review Model"""
        place_id = ""
        user_id = ""
        text = ""
