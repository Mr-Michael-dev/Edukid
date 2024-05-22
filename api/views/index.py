#!/usr/bin/python3
""" Index """
from models.user import User
from models.watch_history import WatchHistory
from models.saved_videos import SavedVideos
from models import storage
from api.views import api_views
from flask import jsonify


@api_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@api_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [WatchHistory, SavedVideos, User]
    names = ["watch_history", "saved_videos", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
