#!/usr/bin/python3
""" holds class User"""

import models
from flask_login import UserMixin
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash
import bcrypt


class User(UserMixin, BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'user'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        full_name = Column(String(128), nullable=True)
        username = Column(String(128), nullable=True, unique=True)
        saved_video = relationship("SavedVideos", backref="user")
        watch_history = relationship("WatchHistory", backref="user")
    else:
        email = ""
        password = ""
        full_name = ""
        username = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    """
    Code source for lines 36 - 52: https://github.com/ploomber/doc/blob/main/examples/flask/login/models.py
    """
    @classmethod
    def get_by_password(cls, *, email, password):
        """returns the user object after checking password match"""
        user = cls.query.filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode("utf-8"), user.password):
            return user
        return None

    @classmethod
    def get_by_id(cls, id):
        """returns the user id"""
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def with_password(cls, *, email, password, full_name, username):
        """initializes a user with hashed password"""
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
        return cls(email=email, password=password_hashed,
                   full_name=full_name, username=username)
