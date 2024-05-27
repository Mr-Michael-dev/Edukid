#!/usr/bin/python
""" holds class SavedVideos"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class SavedVideos(BaseModel, Base):
    """Representation of SavedVideos """
    if models.storage_t == 'db':
        __tablename__ = 'saved_videos'
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        video_id = Column(String(60), nullable=False)
        video_url = Column(String(60), nullable=True)
        title = Column(String(200), nullable=False)
        thumbnail = Column(String(200), nullable=False)
    else:
        user_id = ""
        video_id = ""
        video_url = ""
        title = ""
        thumbnail = ""

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
