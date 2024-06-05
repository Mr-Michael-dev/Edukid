#!/usr/bin/python3
""" route for viewing profile"""
from flask import render_template
from models.saved_videos import SavedVideos
from web_routes import web_routes
from flask_login import login_required, current_user
from models import storage


@web_routes.route('/profile')
@login_required
def user_profile():
    """displays the user profile"""
    user = {
        'full_name': current_user.full_name,
        'username': current_user.username
    }

    saved_videos = storage._DBStorage__session.query(SavedVideos).filter_by(
        user_id=current_user.id).all()
    return render_template('profile.html', user=user, videos=saved_videos)
