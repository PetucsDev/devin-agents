# Perfil: Python Flask

## Stack

- Lenguaje: Python 3.10+
- Framework: Flask
- Build tool: pip / poetry / uv
- Tests: pytest + Flask test client
- Persistencia: SQLAlchemy, Flask-SQLAlchemy u otro ORM segun el proyecto
- Contenedores: Docker

## Deteccion

Se activa con `requirements.txt`, `pyproject.toml` o `poetry.lock` que contengan `flask` y no contengan `django` ni `fastapi`.

## Comandos de validacion

- Instalar: `pip install -r requirements.txt` o `poetry install`
- Tests: `pytest`
- Lint: `ruff check .` o `flake8`
- Type check: `mypy .`

## Archivos de verificacion obligatoria

Antes de proponer cambios, lee y considera:

- `README.md` y `.ai-agents.yaml`.
- `pyproject.toml`, `requirements.txt` o `poetry.lock`.
- Entrypoint de la app (`app.py`, `main.py`, `wsgi.py`, `factory.py`).
- Blueprints y estructura de carpetas.
- Modelos (`models.py`) si existen.
- Tests existentes (`tests/` o `test_*.py`).
- No inventes blueprints, modelos, schemas ni dependencias que no aparezcan en estos archivos.

## Convenciones

- Uso de blueprints para organizar rutas por dominio.
- App factory (`create_app`) cuando el proyecto tiene tests o multiples configuraciones.
- Logica de negocio fuera de las rutas (services/helpers).
- Manejo de errores con `@app.errorhandler` o equivalente.
- Tests con el test client de Flask.

## Anti-patrones a evitar

- Logica de negocio en rutas.
- Estado global mutable fuera de la app factory.
- No manejar excepciones HTTP y devolver HTML por defecto en APIs.
- Imports circulares entre blueprints y modelos.
- Depender de configuracion hardcodeada en lugar de variables de entorno.
