from datetime import datetime
from flask import Blueprint, jsonify, request
from app import db
from app.models.prestamo import Prestamo

prestamos_bp = Blueprint("prestamos", __name__, url_prefix="/prestamos")


@prestamos_bp.route("", methods=["POST"])
def crear_prestamo():
    data = request.get_json()
    if not data or not data.get("libro_id") or not data.get("usuario_nombre"):
        return jsonify({"error": "Los campos 'libro_id' y 'usuario_nombre' son requeridos"}), 400

    prestamo = Prestamo(
        libro_id=data["libro_id"],
        usuario_nombre=data["usuario_nombre"],
    )
    db.session.add(prestamo)
    db.session.commit()
    return jsonify(prestamo.to_dict()), 201


@prestamos_bp.route("/<int:id>/devolver", methods=["PATCH"])
def devolver_prestamo(id):
    prestamo = Prestamo.query.get(id)
    if not prestamo:
        return jsonify({"error": "Préstamo no encontrado"}), 404

    prestamo.estado = "devuelto"
    prestamo.fecha_devolucion = datetime.utcnow()
    db.session.commit()
    return jsonify(prestamo.to_dict()), 200
