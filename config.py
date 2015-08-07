import os
from app import app

WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# app.config['SECRET_KEY'] = 'top secret!'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['OAUTH_CREDENTIALS'] = {
    'google': {
        'id': '447611941974-at5a27b0qjgkujc3ra3go4jdf6csu4b6.apps.googleusercontent.com',
        'secret': 'wh51exbfMZgva1YQfMTu8h1x'
    }
}