from flask import Blueprint, jsonify, request
from app import db
from app.models.libro import Libro

libros_bp = Blueprint("libros", __name__, url_prefix="/libros")


@libros_bp.route("", methods=["POST"])
def registrar_libro():
    data = request.get_json()
    if not data or not data.get("titulo") or not data.get("autor") or data.get("cantidad_total") is None:
        return jsonify({"error": "Los campos 'titulo', 'autor' y 'cantidad_total' son requeridos"}), 400

    libro = Libro(
        titulo=data["titulo"],
        autor=data["autor"],
        cantidad_total=data["cantidad_total"],
        cantidad_disponible=data["cantidad_total"],
    )
    db.session.add(libro)
    db.session.commit()
    return jsonify(libro.to_dict()), 200


@libros_bp.route("/<int:id>", methods=["GET"])
def obtener_libro(id):
    libro = Libro.query.get(id)
    return jsonify(libro.to_dict()), 200
