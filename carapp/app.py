from flask import (
  Flask,
  redirect,
  url_for
)
from carapp.modules import car
from carapp.extensions import (
  db,
  ma,
)
from carapp.models import Car

def blueprints(app):
  app.register_blueprint(car)
  return None


def extensions(app):
  """
  Register 0 or more extensions (mutates the app passed in).

  :param app: Flask application instance
  :return: None
  """
  db.init_app(app)
  ma.init_app(app)
  
  return None

def create_app(settings_override=None):
  """
  Create a Flask application using the app factory pattern.

  :param settings_override: Override settings
  :return: Flask app
  """
  app = Flask(__name__, instance_relative_config=True)
  
  app.config.from_object('config.settings')
  app.config.from_pyfile('settings.py', silent=True)

  if settings_override:
    app.config.update(settings_override)

  extensions(app)
  blueprints(app)
  
  @app.route('/')
  def index():
    """
    Render index page

    :return: Flask response
    """
    return redirect(url_for('car.show'))

  return app