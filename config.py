from os import path

# App details
BASE_DIRECTORY = path.abspath(path.dirname(__file__))
SECRET_KEY = "lock_it_secret"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Credentials
FB_APP_ID = "xxxxxxx"
FB_APP_NAME = "xxxxxxx"
FB_APP_SECRET = "xxxxxxx"
FB_ACCESS_TOKEN_PAGE = 'xxxxxxx'

# Database details
SQLALCHEMY_DATABASE_URI = "{0}{1}".format("sqlite:///", path.join(BASE_DIRECTORY, "app.db"))