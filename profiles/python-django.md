# Perfil: Python Django

## Stack

- Lenguaje: Python 3.10+
- Framework: Django
- Build tool: pip / poetry / uv
- Tests: pytest-django, Django TestCase
- Persistencia: Django ORM (PostgreSQL, SQLite, MySQL segun el proyecto)
- Contenedores: Docker

## Deteccion

Se activa con `requirements.txt`, `pyproject.toml` o `poetry.lock` que contengan `django`, y la existencia de `manage.py`.

## Comandos de validacion

- Instalar: `pip install -r requirements.txt` o `poetry install`
- Tests: `python manage.py test` o `pytest`
- Migraciones: `python manage.py makemigrations --check`
- Lint: `ruff check .` o `flake8`
- Type check (opcional): `mypy .`

## Archivos de verificacion obligatoria

Antes de proponer cambios, lee y considera:

- `README.md` y `.ai-agents.yaml`.
- `manage.py`, `settings.py` (o modulo de settings).
- `pyproject.toml`, `requirements.txt` o `poetry.lock`.
- Estructura de apps bajo la carpeta del proyecto.
- Modelos existentes (`models.py`).
- Tests existentes (`tests.py` o carpeta `tests/`).
- No inventes apps, modelos, vistas, serializers ni dependencias que no aparezcan en estos archivos.

## Convenciones

- Logica de negocio en modelos (`model methods`) o `services.py`, no en vistas.
- Vistas basadas en clases (CBV) o funciones segun el estilo del proyecto.
- Serializers con Django REST Framework si aplica.
- Migraciones reversibles.
- Tests que usen `TestCase` o `pytest-django` y `Client` para endpoints.

## Anti-patrones a evitar

- Logica de negocio en vistas o templates.
- Consultas N+1 sin `select_related`/`prefetch_related`.
- Magic numbers y cadenas sueltas; preferir constantes y settings.
- Migraciones irreversibles o con datos destructivos.
- Hardcodear queries SQL sin necesidad.
