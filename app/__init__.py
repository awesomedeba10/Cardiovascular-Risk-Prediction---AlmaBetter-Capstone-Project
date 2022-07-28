from flask import Flask

app = Flask(__name__, template_folder='html')
app.url_map.strict_slashes = False
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return {'response': str(error)}, 404

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

from app.modules.home.controller import home_blueprint
app.register_blueprint(home_blueprint)