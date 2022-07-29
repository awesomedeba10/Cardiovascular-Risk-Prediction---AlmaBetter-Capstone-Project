from flask import Blueprint, render_template, jsonify

from app import app
from app.helper import *
from app.services.load_models import LoadModel

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@home_blueprint.route('/risk-prediction', methods=['GET'])
def prediction():
    return render_template('prediction.html', models=LoadModel().model_dict)

@home_blueprint.route('/risk-prediction-result', methods=['POST'])
def prediction_result():
    data = request.form

    model = LoadModel()
    result = model.predict(request.form)
    
    return jsonify(result)