# Ejemplo: alucinacion en QA

## Tarea

"Revisa el cambio que agrega el endpoint POST /cards y propone casos de prueba."

## Respuesta incorrecta (alucinacion)

> "El endpoint debe validar que el `cardNumber` tenga 16 digitos, que el `cvv` tenga 3 digitos y que el `expirationDate` sea futuro. Propongo tests para tarjeta valida, numero corto, cvv invalido, fecha vencida y usuario no autenticado."

Problemas:

- Asume campos del payload (`cardNumber`, `cvv`, `expirationDate`) sin leer el DTO o la documentacion.
- Asume reglas de negocio (16 digitos, 3 digitos, fecha futura) sin evidencia.
- Inventa un escenario de "usuario no autenticado" si no se menciono autenticacion en el cambio.

## Respuesta correcta

> "Leo el diff, el DTO de request y los tests existentes para entender qué se valida realmente."
>
> 1. Reviso el codigo del endpoint y el DTO/Pydantic/schema usado.
> 2. Identifico qué validaciones estan implementadas vs. las que podrian faltar.
> 3. Propongo casos de prueba basados unicamente en el comportamiento observable del cambio.
> 4. Distingo entre "el codigo valida X" y "faltaria validar Y".
> 5. Si falta contexto de negocio, lo declaro como pregunta abierta.
>
> No propongo casos que dependan de campos o reglas que no aparecen en el codigo revisado.

## Leccion

Los casos de prueba deben surgir del codigo y documentacion revisados, no de supuestos generales sobre dominios de tarjetas o autenticacion.
