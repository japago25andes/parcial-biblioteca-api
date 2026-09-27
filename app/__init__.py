import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql+psycopg2://{os.environ.get('DB_USER', 'biblioteca_user')}"
        f":{os.environ.get('DB_PASSWORD', 'biblioteca_pass')}"
        f"@{os.environ.get('DB_HOST', 'localhost')}"
        f":{os.environ.get('DB_PORT', '5432')}"
        f"/{os.environ.get('DB_NAME', 'biblioteca_db')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from sqlalchemy.exc import IntegrityError

    @app.errorhandler(IntegrityError)
    def handle_integrity_error(e):
        db.session.rollback()
        return {"error": "Error de integridad en la base de datos", "detalle": str(e.orig)}, 500

    from app.routes.libros import libros_bp
    from app.routes.prestamos import prestamos_bp

    app.register_blueprint(libros_bp)
    app.register_blueprint(prestamos_bp)

    with app.app_context():
        db.create_all()

    return app
