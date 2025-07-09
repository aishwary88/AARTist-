from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'

    from routes import main  # changed from .routes to routes
    app.register_blueprint(main)

    return app