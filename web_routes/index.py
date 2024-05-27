#!/usr/bin/python3
""" route for the homepage"""
from flask import render_template
from web_routes import web_routes
from get_videos import get_videos


@web_routes.route('/', methods=['GET'])
def index():
    """ render the home page """
    query ='maths, english for kids'
    videos = get_videos(query)
    return render_template('index.html', videos=videos)
