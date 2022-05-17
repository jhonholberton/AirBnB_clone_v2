#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states', cascade='all, delete')
    else:
        @property
        def cities(self):
            """Cities Method"""
            from models import storage
            from models.city import City

            cities = storage.all(City).values()
            list_to_return = []
            for value in cities:
                if value.state_id == self.id:
                    list_to_return.append(value)
            return list_to_return
