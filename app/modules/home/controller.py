from flask import Blueprint, render_template, url_for

from app import app
from app.helper import *

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@home_blueprint.route('/risk-prediction', methods=['GET'])
def prediction():
    return render_template('prediction.html')

@home_blueprint.route('/risk-prediction-result', methods=['POST'])
def prediction_result():
    data = request.form
    print(data)