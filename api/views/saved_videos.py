#!/usr/bin/python3
""" objects that handles all default RestFul API actions for saved_videos """
from models.saved_videos import SavedVideos
from models.user import User
from models import storage
from api.views import api_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@api_views.route('/users/<user_id>/saved_videos', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/saved_videos/saved_videos_by_user.yml',
           methods=['GET'])
def get_saved_videos(user_id):
    """
    Retrieves the list of all saved_videos objects
    of a specific User, or a specific saved_video
    """
    list_saved_videos = []
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    for saved_videos in user.saved_videos:
        list_saved_videos.append(saved_videos.to_dict())

    return jsonify(list_saved_videos)


@api_views.route('/get_saved_videos/<saved_video_id>/',
                 methods=['GET'], strict_slashes=False)
@swag_from('documentation/saved_videos/get_saved_video.yml', methods=['GET'])
def get_saved_video(saved_video_id):
    """
    Retrieves a specific saved_video based on id
    """
    saved_videos = storage.get(SavedVideos, saved_video_id)
    if not saved_videos:
        abort(404)
    return jsonify(saved_videos.to_dict())


@api_views.route('/get_saved_videos/<saved_video_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/saved_videos/delete_saved_video.yml',
           methods=['DELETE'])
def delete_saved_video(saved_video_id):
    """
    Deletes a saved_video based on id provided
    """
    saved_videos = storage.get(SavedVideos, saved_video_id)

    if not saved_videos:
        abort(404)
    storage.delete(saved_videos)
    storage.save()

    return make_response(jsonify({}), 200)


@api_views.route('/users/<user_id>/saved_videos', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/saved_videos/post_saved_video.yml', methods=['POST'])
def post_saved_video(user_id):
    """
    Creates a SavedVideo
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
    instance = SavedVideos(**data)
    instance.user_id = user.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)
