# Ejemplo: test de integracion

## Tarea

"Agregar un test de integracion para el endpoint POST /cards."

## Respuesta esperada

1. Buscar tests de integracion existentes como referencia.
2. Crear clase `CardControllerIntegrationTest`.
3. Usar Testcontainers para la base de datos si aplica.
4. Preparar datos, ejecutar request y validar respuesta y estado.
5. Ejecutar `mvn failsafe:integration-test`.
6. Reportar resultado.
