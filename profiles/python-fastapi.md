# Perfil: Python FastAPI

## Stack

- Lenguaje: Python 3.10+
- Framework: FastAPI
- Build tool: pip / poetry / uv
- Tests: pytest
- Persistencia: SQLAlchemy, TortoiseORM o motor a definir
- Contenedores: Docker

## Deteccion

Se activa con `requirements.txt`, `pyproject.toml` o `poetry.lock` que contengan `fastapi`.

## Comandos de validacion

- Instalar: `pip install -r requirements.txt` o `poetry install`
- Tests: `pytest`
- Lint: `ruff check .` o `flake8`
- Type check: `mypy .`

## Convenciones

- Esquemas Pydantic para request/response.
- Dependencias de FastAPI para inyeccion.
- Routers por dominio.
- Tests con pytest y TestClient de FastAPI.

## Anti-patrones a evitar

- Logica de negocio en endpoints.
- No manejar excepciones HTTP.
- Imports circulares.
