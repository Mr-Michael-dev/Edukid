#!/usr/bin/python3
""" Blueprint for web routes """
from flask import Blueprint

web_routes = Blueprint('web_routes', __name__)

from web_routes.user_manager import *
from web_routes.index import *
from web_routes.view_video import *
#from web_routes.watch_history import *
from web_routes.saved_videos import *
from web_routes.profile import *
