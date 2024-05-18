#!/usr/bin/python3
"""
Contains the test for WatchHistory classes
"""

import models
from models import watch_history
from models.base_model import BaseModel
import unittest
WatchHistory = watch_history.WatchHistory


class TestWatchHistory(unittest.TestCase):
    """Test the WatchHistory class"""
    def test_is_subclass(self):
        """Test that WatchHistory is a subclass of BaseModel"""
        watch_history = WatchHistory()
        self.assertIsInstance(watch_history, BaseModel)
        self.assertTrue(hasattr(watch_history, "id"))
        self.assertTrue(hasattr(watch_history, "created_at"))
        self.assertTrue(hasattr(watch_history, "updated_at"))

    def test_user_id_attr(self):
        """Test that WatchHistory has attr user_id, and it's an empty string"""
        watch_history = WatchHistory()
        self.assertTrue(hasattr(watch_history, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(watch_history.user_id, None)
        else:
            self.assertEqual(watch_history.user_id, "")

    def test_video_id_attr(self):
        """
        Test that WatchHistory has attr video_id, and it's an empty string
        """
        watch_history = WatchHistory()
        self.assertTrue(hasattr(watch_history, "video_id"))
        if models.storage_t == 'db':
            self.assertEqual(watch_history.video_id, None)
        else:
            self.assertEqual(watch_history.video_id, "")

    def test_video_url_attr(self):
        """
        Test that WatchHistory has attr video_url, and it's an empty string
        """
        watch_history = WatchHistory()
        self.assertTrue(hasattr(watch_history, "video_url"))
        if models.storage_t == 'db':
            self.assertEqual(watch_history.video_url, None)
        else:
            self.assertEqual(watch_history.video_url, "")

    def test_title_attr(self):
        """Test that WatchHistory has attr title, and it's an empty string"""
        watch_history = WatchHistory()
        self.assertTrue(hasattr(watch_history, "title"))
        if models.storage_t == 'db':
            self.assertEqual(watch_history.title, None)
        else:
            self.assertEqual(watch_history.title, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        vid = WatchHistory()
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
        vid = WatchHistory()
        new_d = vid.to_dict()
        self.assertEqual(new_d["__class__"], "WatchHistory")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"],
                         vid.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"],
                         vid.updated_at.strftime(t_format))

    def test_str(self):
        """
        test that the str method has the correct output
        """
        watch_history = WatchHistory()
        string = "[WatchHistory] ({}) {}".format(
            watch_history.id, watch_history.__dict__)
        self.assertEqual(string, str(watch_history))
