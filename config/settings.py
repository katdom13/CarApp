import os
from datetime import timedelta

DEBUG = True
SECRET_KEY = b'dc9Es7eHxCRxaV282zXBK8o38ejrD/8c'
db_uri = 'sqlite:///' +os.path.abspath(os.path.join(os.getcwd(), '..', 'carapp', 'carapp'))
SQLALCHEMY_DATABASE_URI = '{0}.db'.format(db_uri)
SQLALCHEMY_TRACK_MODIFICATIONS = False