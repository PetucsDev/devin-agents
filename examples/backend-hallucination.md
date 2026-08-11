# Ejemplo: alucinacion en backend

## Tarea

"Agrega un endpoint GET /cards/{id} que devuelva el detalle de una tarjeta."

## Respuesta incorrecta (alucinacion)

> "Agrego el metodo `getCardById` en `CardController`. Uso el `CardService.findById(id)` y el repositorio `CardRepository.findById(id)`. Retorno un `CardDetailDTO` con los campos `number`, `holderName`, `expirationDate` y `cvv`. Tambien agrego el test `CardControllerTest.getCardByIdShouldReturn200`.

Problemas:

- Inventa `CardService.findById`, `CardRepository.findById` y `CardDetailDTO` sin verificar si existen.
- Decide campos del DTO sin ver el dominio real.
- Cita un test sin saber si existe la clase `CardControllerTest`.

## Respuesta correcta

> "Primero leo el controlador, servicios, repositorios y tests existentes para entender el dominio y las convenciones del proyecto."
>
> 1. `read_file` de `CardController` (o buscar controladores con `grep_search` si no se el nombre exacto).
> 2. `grep_search` de `CardService`, `CardRepository`, `CardDTO` para ver que existe.
> 3. Verifico `pom.xml`/`build.gradle` por dependencias de validacion/web.
> 4. Implemento el endpoint siguiendo el estilo existente.
> 5. Ejecuto el comando de test del perfil.
> 6. Respondo con citas absolutas y rangos de lineas.
>
> Si `CardService` no existe, declaro que debo crearlo o adaptar el endpoint a la capa que el proyecto tenga.

## Leccion

Nunca asumas nombres de servicios, repositorios, DTOs ni campos. Lee el codigo real o declara que no lo encontraste.
