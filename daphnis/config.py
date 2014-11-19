import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'kimlur9Glur6Inmid5Slodu'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db') # move from here
CSRF_ENABLED = True
