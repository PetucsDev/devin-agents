# Ejemplo: alucinacion en testing

## Tarea

"Agrega un test unitario para `CardService.createCard`."

## Respuesta incorrecta (alucinacion)

> "Creo `CardServiceTest` con el metodo `createCardShouldReturnCard`. Uso `MockitoAnnotations.openMocks(this)`, mockeo `CardRepository` con `@Mock` y inyecto con `@InjectMocks`. Llamo a `cardService.createCard(cardRequest)` y verifico con `assertThat(result).isEqualTo(expectedCard)`.

Problemas:

- Inventa nombres (`CardRequest`, `expectedCard`, `Card`) sin ver el codigo real.
- Asume el framework de assertions (`assertThat(...).isEqualTo(...)`) sin saber si usan AssertJ, Hamcrest u otro.
- Asume anotaciones de Mockito/JUnit sin leer tests existentes.

## Respuesta correcta

> "Busco tests existentes del mismo servicio o similares para copiar el estilo, luego leo `CardService`."
>
> 1. `grep_search` de `CardServiceTest` o `*ServiceTest`.
> 2. `read_file` del test de referencia para ver anotaciones, assertions y helpers.
> 3. `read_file` de `CardService` para conocer la firma real de `createCard`.
> 4. Escribo el test con el mismo estilo y librerias del proyecto.
> 5. Ejecuto `mvn test` u otro comando del perfil.
>
> Si el proyecto no tiene AssertJ, no lo introduzco solo por costumbre.

## Leccion

Los tests nuevos deben seguir las convenciones reales del proyecto. No inventes firmas de metodos ni importes librerias que no estan en uso.
