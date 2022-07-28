from app import app
import os

if __name__ == '__main__':
    app.run(host=app.config.get('APP_HOST', '127.0.0.1'),
    port=int(app.config.get('APP_PORT', 5000)),
    debug=app.config.get('APP_DEBUG', False))