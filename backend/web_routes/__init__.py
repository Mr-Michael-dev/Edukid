#!/usr/bin/python3
""" Blueprint for web routes """
from flask import Blueprint

web_routes = Blueprint('web_routes', __name__)

from web_routes.home import *