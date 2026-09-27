from app import db


class Libro(db.Model):
    __tablename__ = "libros"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(150), nullable=False)
    cantidad_total = db.Column(db.Integer, nullable=False)
    cantidad_disponible = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "cantidad_total": self.cantidad_total,
            "cantidad_disponible": self.cantidad_disponible,
        }
