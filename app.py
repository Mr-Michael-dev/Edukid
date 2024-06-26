#!/usr/bin/python3
"""
entry point of my flask app
"""
from models import storage
import os
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from api.views import api_views
from web_routes import web_routes
from flask import Flask, make_response, jsonify, render_template
from flask_login import LoginManager
from flask_cors import CORS
from flasgger import Swagger
import logging
from flask_migrate import Migrate

app = Flask("__name__")
app.config['SECRET_KEY'] = os.getenv('EDUKID_SECRET_KEY')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set the SQLAlchemy database URI from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(
    os.getenv('EDUKID_MYSQL_USER'),
    os.getenv('EDUKID_MYSQL_PWD'),
    os.getenv('EDUKID_MYSQL_HOST'),
    os.getenv('EDUKID_MYSQL_DB')
)

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
db.session = storage._DBStorage__session
migrate = Migrate(app, db)

# Configure logging
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

app.register_blueprint(api_views)
app.register_blueprint(web_routes)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SWAGGER'] = {
    'title': 'Edukid API',
    'uiversion': 1
}
Swagger(app)

"""setup login manager"""
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'web_routes.login'
login_manager.login_message = 'You are not logged in'


@login_manager.user_loader
def load_user(user_id):
    """
    Authenticate users when performing requests via the browser. Authentication
    management is handled by flask-login.
    """
    return storage._DBStorage__session.query(User).get(user_id)


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


@app.errorhandler(500)
def server_error(error):
    """500 error"""
    return render_template('500.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
