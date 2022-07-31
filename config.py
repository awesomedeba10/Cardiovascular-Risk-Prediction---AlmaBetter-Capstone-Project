import os

APP_ENV = 'Development'
APP_HOST = '0.0.0.0'
APP_PORT = os.getenv('PORT') or 5000 # if local env is not set
APP_DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'models')
DATA_DIR = os.path.join(BASE_DIR, 'data')
ASSET_DIR = os.path.join(BASE_DIR, 'app', 'static')

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True
CSRF_SESSION_KEY = "12d9fe4214e5d2a5001fa3a0d7800a480dfaaea3"

# Secret key for signing cookies
SECRET_KEY = "51ac0a33945f0c09670d2f2917e3e8c0"