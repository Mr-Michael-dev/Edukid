#!/usr/bin/python3
""" route for the homepage"""
from flask import render_template
from web_routes import web_routes
from get_videos import get_videos


@web_routes.route('/', methods=['GET'])
def index():
    """ render the home page """
    import random
    try:
        SAFE_SEARCH_TERMS = ['kids science', 'animal education for kid', 'kids art', 'english for teens', 'maths for teens']
        query = random.choice(SAFE_SEARCH_TERMS)
        videos = get_videos(query)
    except Exception:
        return render_template('500.html')
    return render_template('index.html', videos=videos)
