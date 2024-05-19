#!/usr/bin/python
""" holds class WatchHistory"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class WatchHistory(BaseModel, Base):
    """Representation of Review """
    if models.storage_t == 'db':
        __tablename__ = 'watch_history'
        user_id = Column(String(60), ForeignKey('User.id'), nullable=False)
        video_id = Column(String(60), nullable=False)
        video_url = Column(String(60), nullable=False)
        title = Column(String(128), nullable=False)
    else:
        user_id = ""
        video_id = ""
        video_url = ""
        title = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
