from flask import Blueprint

def register_blueprints(app):
    # Aquí irán los blueprints
    from .main_routes import main_bp
    app.register_blueprint(main_bp)
