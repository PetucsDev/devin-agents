#!/usr/bin/env python3
"""Valida la estructura minima del repositorio devin-agents.

Requiere PyYAML para validar config/default.yaml. Instalar con:
    pip install pyyaml
"""

import sys
from pathlib import Path

try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_PROFILE_SECTIONS = [
    "Stack",
    "Deteccion",
    "Comandos de validacion",
    "Archivos de verificacion obligatoria",
    "Convenciones",
    "Anti-patrones a evitar",
]

REQUIRED_PROMPT_REFERENCES = [
    "_base.md",
    "hallucination-guardrails.md",
]

REQUIRED_EXAMPLE_ROLES = ["backend", "testing", "devops", "qa", "avoid-hallucination"]


def validate_profiles() -> list[str]:
    profiles_dir = REPO_ROOT / "profiles"
    errors: list[str] = []
    for profile in sorted(profiles_dir.glob("*.md")):
        text = profile.read_text(encoding="utf-8")
        for section in REQUIRED_PROFILE_SECTIONS:
            if f"## {section}" not in text:
                errors.append(f"{profile.name}: falta seccion '{section}'")
    return errors


def validate_prompts() -> list[str]:
    prompts_dir = REPO_ROOT / "prompts"
    errors: list[str] = []
    for prompt in sorted(prompts_dir.glob("*.md")):
        if prompt.name == "_base.md":
            continue
        text = prompt.read_text(encoding="utf-8")
        for ref in REQUIRED_PROMPT_REFERENCES:
            if ref not in text:
                errors.append(f"{prompt.name}: no referencia '{ref}'")
    return errors


def validate_yaml_config() -> list[str]:
    if not HAS_YAML:
        return ["PyYAML no esta instalado; no se pudo validar config/default.yaml"]

    config = REPO_ROOT / "config" / "default.yaml"
    errors: list[str] = []
    try:
        data = yaml.safe_load(config.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"config/default.yaml: YAML invalido - {exc}"]

    if not isinstance(data, dict):
        return ["config/default.yaml: el contenido no es un diccionario"]

    if "stack_detection" not in data:
        errors.append("config/default.yaml: falta clave 'stack_detection'")
    else:
        profiles = data["stack_detection"].get("profiles", {})
        if not profiles:
            errors.append("config/default.yaml: 'stack_detection.profiles' esta vacio")
        for name, spec in profiles.items():
            if not isinstance(spec, dict) or "evidence" not in spec:
                errors.append(
                    f"config/default.yaml: perfil '{name}' sin clave 'evidence'"
                )
            else:
                for item in spec["evidence"]:
                    if not isinstance(item, dict) or "file" not in item or "must_contain" not in item:
                        errors.append(
                            f"config/default.yaml: evidencia de '{name}' invalida: {item}"
                        )
    return errors


def validate_examples() -> list[str]:
    examples_dir = REPO_ROOT / "examples"
    errors: list[str] = []
    names = {p.name for p in examples_dir.glob("*.md")}
    for role in REQUIRED_EXAMPLE_ROLES:
        if not any(role in n for n in names):
            errors.append(f"examples/: falta ejemplo relacionado con '{role}'")
    return errors


def validate_knowledge() -> list[str]:
    knowledge_dir = REPO_ROOT / "knowledge"
    required_non_empty = [
        "architecture-review.md",
        "common-pitfalls.md",
        "testing-standards.md",
        "hallucination-guardrails.md",
    ]
    required_optional_content = [
        "agent-failures.md",
    ]
    errors: list[str] = []

    for name in required_non_empty:
        path = knowledge_dir / name
        if not path.exists():
            errors.append(f"knowledge/{name}: no existe")
        elif path.stat().st_size == 0:
            errors.append(f"knowledge/{name}: esta vacio")

    for name in required_optional_content:
        path = knowledge_dir / name
        if not path.exists():
            errors.append(f"knowledge/{name}: no existe")

    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_profiles())
    errors.extend(validate_prompts())
    errors.extend(validate_yaml_config())
    errors.extend(validate_examples())
    errors.extend(validate_knowledge())

    if errors:
        print("Errores encontrados:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Validacion OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
