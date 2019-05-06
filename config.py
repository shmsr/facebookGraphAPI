from os import path

# App details
BASE_DIRECTORY = path.abspath(path.dirname(__file__))
SECRET_KEY = "keep_it_like_a_secret"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Credentials
FB_APP_ID = "605837159915772"
FB_APP_NAME = "OneDirectCX"
FB_APP_SECRET = "4ae4a05414fb68e97420197edced7a04"
FB_ACCESS_TOKEN_PAGE = 'EAAInAXS1YPwBANsEB921uXOE8PTWrKcdI7spWbYxwcmpvssgwcHnBBLXaO1brQmfRXaf0nMMPChwZAf1nCstlv9QgVRFol81WMiHEbqMzj3DVcA4F3s0PWuHEHttLpPRhxATWJTlS3AWF4xM0sbsuZBjmx3ylIPhpKAY4sLcZAsK3OjonfT'

# Database details
SQLALCHEMY_DATABASE_URI = "{0}{1}".format("sqlite:///", path.join(BASE_DIRECTORY, "app.db"))