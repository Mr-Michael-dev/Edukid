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
        password = Column(String(128), nullable=False)
        full_name = Column(String(128), nullable=False)
        username = Column(String(128), nullable=False, unique=True)
        saved_video = relationship("SavedVideos", backref="user")
        watch_history = relationship("WatchHistory", backref="user")
    else:
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
    def with_password(cls, *, password, full_name, username):
        """initializes a user with hashed password"""
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
        return cls(password=password_hashed,
                   full_name=full_name, username=username)
