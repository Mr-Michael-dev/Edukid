#!/usr/bin/python
""" holds class SavedVideos"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class SavedVideos(BaseModel, Base):
    """Representation of SavedVideos """
    if models.storage_t == 'db':
        __tablename__ = 'saved_videos'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        video_id = Column(String(60), nullable=False)
        video_url = Column(String(60), nullable=False)
        title = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
    else:
        user_id = ""
        video_id = ""
        video_url = ""
        title = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
