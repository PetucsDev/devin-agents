# Ejemplo: respuesta con alucinacion y su correccion

## Tarea

"Agrega validacion al endpoint POST /cards para que rechace numeros de tarjeta vacios."

## Respuesta incorrecta (alucinacion)

> "Modifico el `CardController` para que use el `CardValidator` que ya existe en `src/main/java/com/example/validation/CardValidator.java`. Ajusto el metodo `createCard` llamando a `cardValidator.validate(dto)` y agrego un test en `CardControllerTest`.

Problemas:

- Inventa la clase `CardValidator` y su ruta sin verificar.
- Inventa la firma `cardValidator.validate(dto)`.
- Cita un test sin saber si existe.
- No lee el codigo real del controlador.

## Respuesta correcta

> "Primero leo el controlador y los tests existentes para entender la estructura actual."
>
> 1. `read_file` del controlador que maneja `POST /cards`.
> 2. `grep_search` de tests relacionados con `CardController`.
> 3. Verifico en `pom.xml`/`build.gradle` si hay dependencias de validacion (Bean Validation, class-validator, etc.).
> 4. Implemento la validacion siguiendo el patron ya usado en el proyecto.
> 5. Ejecuto el comando de test del perfil.
> 6. Respondo con citas exactas de archivos y lineas.
>
> Si no encuentro una clase `CardValidator`, no la invento; agrego la validacion en el lugar que el codigo real indique.

## Leccion

Antes de proponer cambios, lee el codigo real y verifica la existencia de clases, metodos y tests. No completes la respuesta con datos inventados.
