from datetime import datetime
from app import db


class Prestamo(db.Model):
    __tablename__ = "prestamos"

    id = db.Column(db.Integer, primary_key=True)
    libro_id = db.Column(db.Integer, db.ForeignKey("libros.id"), nullable=False)
    usuario_nombre = db.Column(db.String(150), nullable=False)
    estado = db.Column(db.String(20), nullable=False, default="prestado")
    fecha_prestamo = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_devolucion = db.Column(db.DateTime)

    libro = db.relationship("Libro")

    def to_dict(self):
        return {
            "id": self.id,
            "libro_id": self.libro_id,
            "usuario_nombre": self.usuario_nombre,
            "estado": self.estado,
            "fecha_prestamo": self.fecha_prestamo.isoformat() if self.fecha_prestamo else None,
            "fecha_devolucion": self.fecha_devolucion.isoformat() if self.fecha_devolucion else None,
        }
