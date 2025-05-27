from .main_routes import main_bp
from .cliente_routes import cliente_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(cliente_bp)
