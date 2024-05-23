#!/usr/bin/python3
""" route for the homepage"""
from flask import render_template, url_for
from web_routes import web_routes
from get_videos import get_videos


@web_routes.route('/', methods=['GET'])
def index():
    """ render the home page """
    query ='maths, english for kids'
    videos = get_videos(query)
    return render_template('index.html', videos=videos)

@web_routes.route('/video/<video_id>')
def view_video(video_id):
    videos = get_videos('maths, english for kids')
    video = next((video for video in videos if video['video_id'] == video_id), None)
    if video:
        return render_template('view_video.html', video=video)
    else:
        return  render_template('404.html')