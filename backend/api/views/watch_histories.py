#!/usr/bin/python3
""" objects that handles all default RestFul API actions for watch_history """
from models.watch_history import WatchHistory
from models.user import User
from models import storage
from api.views import api_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@api_views.route('/users/<user_id>/watch_history', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/watch_history/watch_history_by_user.yml',
           methods=['GET'])
def get_watch_history(user_id):
    """
    Retrieves the list of all watch_history objects
    of a specific User, or a specific watch_history
    """
    list_watch_history = []
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    for watch_history in user.watch_history:
        list_watch_history.append(watch_history.to_dict())

    return jsonify(list_watch_history)


@api_views.route('/watch_history/<watch_history_id>/',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/watch_history/get_watch_history.yml',
           methods=['GET'])
def get_watch_history(watch_history_id):
    """
    Retrieves a specific watch_history based on id
    """
    watch_history = storage.get(WatchHistory, watch_history_id)
    if not watch_history:
        abort(404)
    return jsonify(watch_history.to_dict())


@api_views.route('/watch_history/<watch_history_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/watch_history/delete_watch_history.yml',
           methods=['DELETE'])
def delete_watch_history(watch_history_id):
    """
    Deletes a watch_history based on id provided
    """
    watch_history = storage.get(WatchHistory, watch_history_id)

    if not watch_history:
        abort(404)
    storage.delete(watch_history)
    storage.save()

    return make_response(jsonify({}), 200)


@api_views.route('/users/<user_id>/watch_history', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/watch_history/post_video.yml', methods=['POST'])
def post_video(user_id):
    """
    Creates a WatchHistoty
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    attr = ['name', 'video_url', 'video_id']
    for i in attr:
        if i not in request.get_json():
            abort(400, description="Missing name")

    data = request.get_json()
    instance = WatchHistory(**data)
    instance.user_id = user.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
