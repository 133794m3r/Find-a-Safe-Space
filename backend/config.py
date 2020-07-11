import os
DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#not used right now.
CSRF_ENABLED    = True
#Same here for session cookies.
SECRET_KEY = os.getenv("SECRET_KEY")
SESSION_TYPE="filesystem"
SESSION_FILE_DIR = "/tmp/flask_sessions/nhwt"
SECRET=os.getenv("SECRET")
MYSQL_CREDS="mysql://{0}@localhost/connect_together?charset=utf8mb4".format(os.getenv('MYSQL_CREDS'))
PSQL_CREDS="postgresql://{0}@localhost/connect_together".format(os.getenv('PSQL_CREDS'))
