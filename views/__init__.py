from .auth_view import auth_bp
from .prenda_view import prenda_bp

def register_blueprint(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(prenda_bp)
    