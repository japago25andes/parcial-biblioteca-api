# 📚 API Biblioteca

API REST simple para gestión de préstamos de una biblioteca, construida con **Python + Flask + PostgreSQL**.
Diseñada para la práctica de **pruebas de software** (parcial).

---

## 📋 Requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y corriendo
- No se necesita instalar Python ni PostgreSQL localmente

---

## 🚀 Levantar el proyecto

```bash
docker compose up
```

El API queda disponible en **`http://localhost:3001`**

Los datos iniciales (libros de ejemplo) se insertan automáticamente al primer arranque.

### Detener
```bash
docker compose down
```

### Resetear base de datos (borrar todo y empezar de cero)
```bash
docker compose down -v
docker compose up
```

---

## 📡 Endpoints

**Base URL:** `http://localhost:3001`

| Método | Ruta | Descripción | Body requerido |
|--------|------|-------------|-----------------|
| POST | `/libros` | Registrar un libro | `titulo` (string), `autor` (string), `cantidad_total` (int) |
| GET | `/libros/:id` | Obtener un libro por id | — |
| POST | `/prestamos` | Crear un préstamo | `libro_id` (int), `usuario_nombre` (string) |
| PATCH | `/prestamos/:id/devolver` | Marcar un préstamo como devuelto | — |

---

## 🧪 Ejemplos con curl

### Registrar un libro
```bash
curl -X POST http://localhost:3001/libros \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Rayuela", "autor": "Julio Cortázar", "cantidad_total": 4}'
```

### Obtener un libro
```bash
curl http://localhost:3001/libros/1
```

### Crear un préstamo
```bash
curl -X POST http://localhost:3001/prestamos \
  -H "Content-Type: application/json" \
  -d '{"libro_id": 1, "usuario_nombre": "María Torres"}'
```

### Devolver un préstamo
```bash
curl -X PATCH http://localhost:3001/prestamos/1/devolver
```

---

## 📐 Estructura de datos

### Libro
```json
{
  "id": 1,
  "titulo": "Cien Años de Soledad",
  "autor": "Gabriel García Márquez",
  "cantidad_total": 3,
  "cantidad_disponible": 3
}
```

### Préstamo
```json
{
  "id": 1,
  "libro_id": 1,
  "usuario_nombre": "María Torres",
  "estado": "prestado",
  "fecha_prestamo": "2026-09-26T10:00:00",
  "fecha_devolucion": null
}
```

### Datos precargados (seed)
| id | titulo | cantidad_total | cantidad_disponible |
|----|--------|-----------------|-----------------------|
| 1 | Cien Años de Soledad | 3 | 3 |
| 2 | 1984 | 2 | 2 |
| 3 | El Principito | 1 | 0 |
