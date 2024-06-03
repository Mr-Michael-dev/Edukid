from flask import render_template, request, flash
from web_routes import web_routes
from get_videos import get_videos

import re  # For regular expression matching

# Configurable list of banned words (replace with your own)
BANNED_WORDS = ['porn', 'violence', 'hate speech', 'sex', 'fight', 'war']

# Alternative safe search terms
SAFE_SEARCH_TERMS = ['science', 'animal education', 'kids art', 'english', 'maths']


@web_routes.route('/search', methods=['POST'])
def search():
    """ Performs search operation with filtering for inappropriate content """
    if request.method == 'POST':
        search_query = request.form['search']

        # Server-side filtering using regular expressions
        filtered_query = search_query
        for word in BANNED_WORDS:
            filtered_query = re.sub(rf'\b{word}\b', '', filtered_query, flags=re.IGNORECASE)

        if filtered_query == '':
            # Choose a random safe search term from the list
            import random
            filtered_query = random.choice(SAFE_SEARCH_TERMS)
            flash('Uh oh! Your search terms seem inappropriate. Here are some suggestions: ' + ', '.join(SAFE_SEARCH_TERMS), category='error')

        # Additional filtering with YouTube Data API safeSearch parameter (optional)
        videos = get_videos(filtered_query)

        return render_template('search.html', videos=videos)
