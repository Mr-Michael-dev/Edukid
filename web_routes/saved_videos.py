#!/usr/bin/python3
""" route for viewing saved video and saving video"""
from models import storage
from flask import render_template, request, jsonify
from models.saved_videos import SavedVideos
from web_routes import web_routes
from flask_login import login_required, current_user


@web_routes.route('/save_video', methods=['POST'])
@login_required
def save_video():
    """saves a video to the database"""
    data = request.get_json()
    video_id = data.get('video_id')
    title = data.get('title')
    thumbnail = data.get('thumbnail')

    if video_id and title and thumbnail:
        saved_video = SavedVideos(user_id=current_user.id,
                                  video_id=video_id, title=title,
                                  thumbnail=thumbnail)
        saved_video.save()
        return jsonify(success=True)
    else:
        return jsonify(success=False), 400


@web_routes.route('/saved_videos')
@login_required
def saved_videos():
    """displays saved videos"""
    saved_videos = storage._DBStorage__session.query(SavedVideos).filter_by(
        user_id=current_user.id).all()
    return render_template('saved_videos.html', videos=saved_videos)
