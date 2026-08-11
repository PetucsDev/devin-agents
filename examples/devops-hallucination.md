# Ejemplo: alucinacion en DevOps

## Tarea

"Actualiza el deployment de Kubernetes para agregar una variable de entorno `DB_HOST`."

## Respuesta incorrecta (alucinacion)

> "Modifico `deployment.yaml` agregando `DB_HOST: postgres.staging.svc.cluster.local` bajo `env`. Tambien actualizo `configmap.yaml` con la misma variable y `secret.yaml` con `DB_PASSWORD`.

Problemas:

- Inventa valores (`postgres.staging.svc.cluster.local`), namespaces y recursos.
- Asume que existen `configmap.yaml` y `secret.yaml` sin verificar.
- Expone un secreto (`DB_PASSWORD`) en lugar de pedir su manejo externo.
- No valida con `kubectl apply --dry-run=client`.

## Respuesta correcta

> "Leo los manifiestos existentes y la configuracion de entornos antes de tocar nada."
>
> 1. `read_file` de `deployment.yaml` y otros manifiestos relevantes.
> 2. Busco si ya hay un ConfigMap o Secret con variables de base de datos.
> 3. Uso un placeholder o referencia a un Secret existente para `DB_HOST`, sin hardcodear valores reales.
> 4. Ejecuto `kubectl apply --dry-run=client -f deployment.yaml` para validar sintaxis.
> 5. Documento el impacto por entorno y dejo valores reales fuera del repo.
>
> Si no encuentro el manifiesto, declaro la ruta antes de crear uno nuevo.

## Leccion

No inventes valores de infraestructura, nombres de servicios ni recursos. Los secretos nunca se hardcodean; se referencian.
