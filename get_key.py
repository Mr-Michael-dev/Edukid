#!/usr/bin/python3
"""gets a secret key"""
import os


def get_key(file):
    """gets a secret key stored in a file"""
    if os.path.isfile(file):  # Check if gapikey is a valid file
        with open(file, 'r') as f:  # Open in read mode
            key = f.read().strip()  # Read and strip whitespace
            return key
    else:
        print("Error: File '{}' not found.".format('file'))
        return None
