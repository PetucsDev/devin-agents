# Revision de arquitectura

Checklist para evaluar cambios de arquitectura en cualquier proyecto.

## Diseno

- El cambio respeta la arquitectura definida del proyecto?
- Se introduce deuda tecnica innecesaria?
- Hay acoplamiento indebido entre capas o modulos?
- Se reutiliza codigo existente o se duplica?

## API y contratos

- Los endpoints o interfaces son claros y consistentes?
- Los DTOs/modelos representan correctamente el dominio?
- Se manejan errores y estados de forma adecuada?

## Persistencia

- Las consultas son eficientes?
- Se evitan N+1 y bloqueos innecesarios?
- Las migraciones son reversibles?

## Seguridad

- Se validan entradas?
- Se manejan secretos correctamente?
- Se aplican los principios de menor privilegio?
