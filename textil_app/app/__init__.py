from flask import Flask
from flask_login import LoginManager
import sirope

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = "super-secret-key"  # Cambiar por una más segura

    # Sirope (usaremos Redis internamente)
    syrup = sirope.Sirope()

    # Login Manager
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # Registro de blueprints (se agregarán más adelante)
    from .routes import register_blueprints
    register_blueprints(app)

    return app
