#!/usr/bin/env python3
"""Scaffold para ejecutar el benchmark de alucinaciones.

Uso basico (verifica contexto y genera reporte):
    python scripts/run_benchmark.py --repo /ruta/a/repo/de/prueba

Para evaluar contra un modelo real, este script debe extenderse con una
invocacion a LLM usando la API que corresponda. Por defecto solo valida
la estructura del benchmark y la existencia de archivos de contexto.

Requiere PyYAML:
    pip install pyyaml
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Error: PyYAML no esta instalado. Ejecuta 'pip install pyyaml'.")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
BENCHMARK_PATH = REPO_ROOT / "evals" / "hallucination-benchmark.yaml"


def load_benchmark(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_context(case: dict[str, Any], repo_path: Path) -> list[str]:
    missing: list[str] = []
    for file in case.get("context", {}).get("files", []):
        if not (repo_path / file).exists():
            missing.append(file)
    return missing


def run_case(case: dict[str, Any], repo_path: Path) -> dict[str, Any]:
    missing_context = check_context(case, repo_path)
    # TODO: invocar al agente/LLM con case["task"] y evaluar la respuesta
    # contra case["success_criteria"] y case["typical_failures"].
    return {
        "id": case["id"],
        "role": case["role"],
        "task": case["task"],
        "missing_context": missing_context,
        "llm_result": None,
        "passed": None,
        "notes": "Scaffold: falta integracion con LLM.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Benchmark anti-alucinacion")
    parser.add_argument(
        "--repo",
        type=Path,
        default=Path("."),
        help="Ruta al repositorio de prueba donde se evaluara el agente.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Archivo JSON donde guardar el reporte.",
    )
    args = parser.parse_args()

    benchmark = load_benchmark(BENCHMARK_PATH)
    results = []
    errors = 0

    for case in benchmark.get("cases", []):
        result = run_case(case, args.repo)
        if result["missing_context"]:
            print(
                f"[AVISO] {case['id']}: faltan archivos de contexto en --repo:"
            )
            for missing in result["missing_context"]:
                print(f"  - {missing}")
            errors += 1
        results.append(result)

    summary = {
        "total_cases": len(results),
        "context_missing": errors,
        "results": results,
    }

    if args.output:
        with args.output.open("w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(f"Reporte guardado en {args.output}")
    else:
        print(json.dumps(summary, indent=2, ensure_ascii=False))

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
