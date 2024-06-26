#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
import models
from models.user import User
from models.saved_videos import SavedVideos
from models.watch_history import WatchHistory
from os import getenv


classes = {"WatchHistory": WatchHistory,
           "SavedVideos": SavedVideos, "User": User}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        EDUKID_MYSQL_USER = getenv('EDUKID_MYSQL_USER')
        EDUKID_MYSQL_PWD = getenv('EDUKID_MYSQL_PWD')
        EDUKID_MYSQL_HOST = getenv('EDUKID_MYSQL_HOST')
        EDUKID_MYSQL_DB = getenv('EDUKID_MYSQL_DB')
        EDUKID_ENV = getenv('EDUKID_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(EDUKID_MYSQL_USER,
                                             EDUKID_MYSQL_PWD,
                                             EDUKID_MYSQL_HOST,
                                             EDUKID_MYSQL_DB))
        if EDUKID_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()
            raise

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database."""
        inspector = inspect(self.__engine)
        for table in Base.metadata.tables.values():
            if not inspector.has_table(table.name):
                table.create(self.__engine)

        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def rollback(self):
        """call rollback() method on the private session attribute"""
        self.__session.rollback()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())
        return count
