#!/usr/bin/python3
""" route for viewing video"""
from flask import render_template, request
from web_routes import web_routes
from flask_login import login_required


@web_routes.route('/video')
def view_video():
    video_id = request.args.get('video_id')
    title = request.args.get('title')

    if video_id and title:
        video = {
            'video_id': video_id,
            'title': title,
        }
        return render_template('view_video.html', video=video)
    else:
        return render_template('404.html')
    