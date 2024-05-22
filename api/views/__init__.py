#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

api_views = Blueprint('api_views', __name__, url_prefix='/api')

from api.views.index import *
from api.views.users import *
from api.views.saved_videos import *
from api.views.watch_histories import *
