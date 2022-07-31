import flask
from flask import Blueprint, render_template, jsonify
import os
from platform import python_version

from app import app
from app.helper import *
from app.services.load_models import LoadModel

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET'])
def index():
    # accessing all charts
    charts_info = get_charts(os.path.join(app.config.get('ASSET_DIR'), 'assets', 'images', 'charts'),
        'assets/images/charts/')

    return render_template('index.html', charts_info=charts_info, python_version=python_version(),
        flask_version=flask.__version__)

@home_blueprint.route('/risk-prediction', methods=['GET'])
def prediction():
    return render_template('prediction.html', models=LoadModel().model_dict)

@home_blueprint.route('/risk-prediction-result', methods=['POST'])
def prediction_result():
    data = request.form

    model = LoadModel()
    result = model.predict(request.form)
    
    return jsonify(result)

@home_blueprint.route('/demo', methods=['GET'])
def demo():
    return render_template('demo.html')