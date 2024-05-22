#!/usr/bin/python3
"""
Contains the test for SavedVideos classes
"""

import models
from models import saved_videos
from models.base_model import BaseModel
import unittest
SavedVideos = saved_videos.SavedVideos


class TestSavedVideos(unittest.TestCase):
    """Test the SavedVideos class"""
    def test_is_subclass(self):
        """Test that SavedVideos is a subclass of BaseModel"""
        saved_videos = SavedVideos()
        self.assertIsInstance(saved_videos, BaseModel)
        self.assertTrue(hasattr(saved_videos, "id"))
        self.assertTrue(hasattr(saved_videos, "created_at"))
        self.assertTrue(hasattr(saved_videos, "updated_at"))
        self.assertTrue(hasattr(saved_videos, "description"))

    def test_user_id_attr(self):
        """Test that SavedVideos has attr user_id, and it's an empty string"""
        saved_videos = SavedVideos()
        self.assertTrue(hasattr(saved_videos, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(saved_videos.user_id, None)
        else:
            self.assertEqual(saved_videos.user_id, "")

    def test_video_id_attr(self):
        """Test that SavedVideos has attr video_id, and it's an empty string"""
        saved_videos = SavedVideos()
        self.assertTrue(hasattr(saved_videos, "video_id"))
        if models.storage_t == 'db':
            self.assertEqual(saved_videos.video_id, None)
        else:
            self.assertEqual(saved_videos.video_id, "")

    def test_video_url_attr(self):
        """
        Test that SavedVideos has attr video_url, and it's an empty string
        """
        saved_videos = SavedVideos()
        self.assertTrue(hasattr(saved_videos, "video_url"))
        if models.storage_t == 'db':
            self.assertEqual(saved_videos.video_url, None)
        else:
            self.assertEqual(saved_videos.video_url, "")

    def test_title_attr(self):
        """Test that SavedVideos has attr title, and it's an empty string"""
        saved_videos = SavedVideos()
        self.assertTrue(hasattr(saved_videos, "title"))
        if models.storage_t == 'db':
            self.assertEqual(saved_videos.title, None)
        else:
            self.assertEqual(saved_videos.title, "")

    def test_description_attr(self):
        """
        Test that SavedVideos has attr description, and it's an empty string
        """
        saved_videos = SavedVideos()
        self.assertTrue(hasattr(saved_videos, "description"))
        if models.storage_t == 'db':
            self.assertEqual(saved_videos.description, None)
        else:
            self.assertEqual(saved_videos.description, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        vid = SavedVideos()
        new_d = vid.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in vid.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        vid = SavedVideos()
        new_d = vid.to_dict()
        self.assertEqual(new_d["__class__"], "SavedVideos")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"],
                         vid.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"],
                         vid.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        saved_videos = SavedVideos()
        string = "[SavedVideos] ({}) {}".format(
            saved_videos.id, saved_videos.__dict__)
        self.assertEqual(string, str(saved_videos))
