# Ejemplo: cambio DevOps

## Tarea

"Actualizar el limite de memoria del deployment de Kubernetes."

## Respuesta esperada

1. Leer el manifiesto `deployment.yaml`.
2. Modificar `resources.limits.memory` y `resources.requests.memory`.
3. Validar sintaxis con `kubectl apply --dry-run=client`.
4. Ejecutar `terraform plan` si hay cambios en infra.
5. Documentar impacto en cada entorno.
6. No tocar el codigo fuente de la aplicacion.
