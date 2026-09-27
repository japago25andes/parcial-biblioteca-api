# 📚 API Biblioteca

API REST simple para gestión de préstamos de una biblioteca, construida con **Python + Flask + PostgreSQL**.

Este proyecto es el **parcial** de la asignatura de Ingeniería de Software III. La API contiene bugs
intencionales que debes encontrar mediante pruebas de caja negra sobre los 4 endpoints, en un máximo
de **2 horas**.

---

## 🎓 Instrucciones de entrega

Individual. Usa las plantillas de la carpeta [`plantillas/`](plantillas/):

- `plantillaPlanDePruebas.xlsx` — un plan de pruebas por endpoint, con todos sus casos de prueba.
- `plantillaCasoDePrueba.docx` — un Word por cada caso de prueba ejecutado.
- `plantillaReporteDeBug.docx` — un Word por cada bug encontrado.

Debes entregar un `.zip` con la siguiente estructura:

```
Nombre_Apellido_Parcial/
  libros-post/
    plan-pruebas.xlsx        # a partir de plantillaPlanDePruebas.xlsx
    caso-01.docx              # a partir de plantillaCasoDePrueba.docx, uno por caso
    caso-02.docx
    ...
  libros-get-id/
    plan-pruebas.xlsx
    caso-01.docx
    ...
  prestamos-post/
    plan-pruebas.xlsx
    caso-01.docx
    ...
  prestamos-devolver/
    plan-pruebas.xlsx
    caso-01.docx
    ...
  bugs-encontrados/
    bug-01.docx               # a partir de plantillaReporteDeBug.docx, uno por bug
    bug-02.docx
    ...
```

Cada Word de **caso de prueba** debe documentar: ID del caso, endpoint, descripción, request enviado,
respuesta esperada, respuesta obtenida, resultado (pasa/falla) y evidencia (captura).

Cada Word de **bug** debe documentar: título del bug, endpoint, pasos para reproducir, resultado
esperado vs. obtenido, severidad y evidencia (captura).

Comprime la carpeta como **`Nombre_Apellido_Parcial.zip`** y envíala por correo a
**johna.pardog@unilibre.edu.co**.

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
