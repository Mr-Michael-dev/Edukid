#!/usr/bin/python3
"""
entry point of my flask app
"""
from models import storage
from api.views import api_views
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

app = Flask("__name__")
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(api_views)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SWAGGER'] = {
    'title': 'Edukid API',
    'uiversion': 1
}
Swagger(app)

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
