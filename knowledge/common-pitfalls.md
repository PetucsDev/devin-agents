# Errores comunes

Lista de problemas recurrentes a detectar y evitar.

## Backend

- Logica de negocio en controladores/handlers.
- Excepciones genericas sin mensaje util.
- Falta de validacion de entradas.
- Acoplamiento con frameworks en el dominio.

## Testing

- Tests que dependen de datos compartidos.
- Mocks que no representan el comportamiento real.
- Tests de integracion sin limpiar estado.
- Ignorar tests fallidos con `@Disabled`/`@Ignore`.

## DevOps

- Secretos hardcodeados en manifiestos.
- Imagenes sin tag fijo o `latest` en produccion.
- Recursos sin limites en Kubernetes.
- Cambios sin rollback plan.

## QA

- Casos de prueba ambiguos.
- Falta de criterios de aceptacion claros.
- No considerar usuarios con datos extremos.
- Descuidar la experiencia de error.
