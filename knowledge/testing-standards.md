# Estandares de testing

Guia para escribir tests de calidad en cualquier stack.

## Principios

- Un test debe fallar por una sola razon.
- Los tests deben ser independientes entre si.
- Usar nombres descriptivos que indiquen comportamiento esperado.
- Cubrir el camino feliz, errores y casos limite.

## Piramide de tests

1. Unitarios: logica pura, mocks de dependencias.
2. Integracion: interaccion con base de datos, colas, servicios externos.
3. E2E: flujos completos, pocos y controlados.

## Determinismo

- No depender de fecha/hora real.
- No depender de orden de ejecucion.
- Limpiar estado entre tests.
- No usar sleeps arbitrarios.

## Cobertura

- La cobertura alta no garantiza calidad.
- Priorizar cobertura de caminos criticos de negocio.
- Eliminar tests triviales que no aportan valor.
