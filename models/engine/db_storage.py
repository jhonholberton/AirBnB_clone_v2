#!/usr/bin/python3

"""
Added new engine: DataBase Storage
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization method"""
        user = os.environ.get('HBNB_MYSQL_USER')
        pas = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,
                                              pas, host, db,
                                              pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary: a list of obj of one type
        """
        cls_name = {"State": State,
                    "City": City,
                    "User": User,
                    "Place": Place,
                    "Review": Review,
                    "Amenity": Amenity}
        obj = {}
        cls_s = [value for key, value in cls_name.items()]
        if cls:
            if type(cls) == str:
                cls = cls_name[cls]
            cls_s = [cls]
        for one_class in cls_s:
            for value in self.__session.query(one_class):
                key = str(value.__class__.__name__) + "." + str(value.id)
                obj[key] = value
        return obj

    def new(self, obj):
        """
        Add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit object to current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete object to current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload objects to current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = scoped_session(Session)

    def close(self):
        """
        Remove the method on the private session attribute
        """
        self.__session.close()
