# Registro de fallos de agentes

Este documento funciona como feedback loop: registra casos reales donde un agente alucino o no siguio las reglas. Con el tiempo, los patrones detectados aqui deben migrarse a `hallucination-guardrails.md`, ajustes en prompts o ejemplos negativos.

## Como registrar un fallo

1. Fecha y rol del agente.
2. Tarea que se le pidio.
3. Comportamiento incorrecto.
4. Archivos o contexto relevante.
5. Causa probable.
6. Accion correctiva aplicada o propuesta.

## Plantilla

```markdown
### YYYY-MM-DD - <rol>

- **Tarea**: ...
- **Comportamiento incorrecto**: ...
- **Contexto**: ...
- **Causa probable**: ...
- **Correccion**: ...
- **Estado**: pendiente / aplicado / descartado
```

## Ejemplo

```markdown
### 2026-08-11 - backend

- **Tarea**: "Agrega un endpoint GET /cards/{id}."
- **Comportamiento incorrecto**: El agente cito `CardService.findById` y `CardRepository.findById`, que no existian en el repo.
- **Contexto**: El proyecto solo tenia `CardController` con logica inline y sin capa de servicio.
- **Causa probable**: El prompt no obligaba a buscar el servicio/repositorio real antes de proponer cambios.
- **Correccion**: Se agrego en `_base.md` el protocolo de grounding y se reforzo en `backend.md` la regla de no inventar servicios.
- **Estado**: aplicado
```

## Registro

| Fecha | Rol | Tarea | Fallo | Correccion | Estado |
|-------|-----|-------|-------|------------|--------|

