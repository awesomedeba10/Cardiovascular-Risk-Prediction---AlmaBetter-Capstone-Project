from app import app

app.run(port=app.config.get('APP_PORT', 5000),
    debug=app.config.get('APP_DEBUG', False))