from app import app
import os

app.run(port=app.config.get('APP_PORT', int(os.environ.get('PORT', 5000))),
    debug=app.config.get('APP_DEBUG', False))