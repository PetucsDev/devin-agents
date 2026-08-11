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
- Tests: `pytest` (o el script definido en `pyproject.toml`)
- Lint: `ruff check .` o `flake8`
- Type check: `mypy .`

## Archivos de verificacion obligatoria

Antes de proponer cambios, lee y considera:

- `README.md` y `.ai-agents.yaml`.
- `pyproject.toml`, `requirements.txt` o `poetry.lock` (versiones de FastAPI, Pydantic, dependencias de testing).
- `pytest.ini`, `setup.cfg` o `tox.ini` si existen.
- Estructura del proyecto (`app/`, `src/`, routers, modelos).
- No inventes routers, modelos Pydantic ni dependencias que no aparezcan en estos archivos.

## Convenciones

- Esquemas Pydantic para request/response.
- Dependencias de FastAPI para inyeccion.
- Routers por dominio.
- Tests con pytest y TestClient de FastAPI.

## Anti-patrones a evitar

- Logica de negocio en endpoints.
- No manejar excepciones HTTP.
- Imports circulares.
