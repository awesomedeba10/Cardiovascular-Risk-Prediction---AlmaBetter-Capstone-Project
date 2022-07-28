from flask import Blueprint, render_template, url_for

from app import app
from app.helper import *

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')