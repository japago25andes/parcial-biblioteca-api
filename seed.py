"""
Script de datos iniciales — Biblioteca.
Se ejecuta automáticamente al levantar el contenedor.
Si los datos ya existen, no los duplica.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from app import create_app, db
from app.models.libro import Libro

app = create_app()

with app.app_context():
    if Libro.query.count() > 0:
        print("Seed: datos ya existen, se omite.")
    else:
        print("Seed: insertando datos iniciales...")

        l1 = Libro(titulo="Cien Años de Soledad", autor="Gabriel García Márquez", cantidad_total=3, cantidad_disponible=3)
        l2 = Libro(titulo="1984", autor="George Orwell", cantidad_total=2, cantidad_disponible=2)
        l3 = Libro(titulo="El Principito", autor="Antoine de Saint-Exupéry", cantidad_total=1, cantidad_disponible=0)
        db.session.add_all([l1, l2, l3])

        db.session.commit()
        print("Seed: listo.")
