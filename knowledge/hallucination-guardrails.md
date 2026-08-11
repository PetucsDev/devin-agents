# Guardrails contra alucinaciones

Este documento define comportamientos que los agentes deben evitar para no inventar informacion, junto con ejemplos de respuestas incorrectas y sus correcciones.

## Definicion

Una alucinacion ocurre cuando el agente:

- Cita un archivo, funcion o parametro que no existe.
- Propone una dependencia, version o configuracion sin verificarla en el repositorio.
- Afirma un comportamiento del codigo sin haberlo leido.
- Inventa un comando de build, test o despliegue que no esta documentado.
- Asume la arquitectura o stack del proyecto sin evidencia.

## Reglas generales

1. **Verificar antes de afirmar**. Si vas a mencionar un archivo, leelo con `read_file`. Si vas a hablar de una dependencia, buscala en `pom.xml`, `package.json`, `go.mod`, `pyproject.toml`, etc.
2. **No completar con datos inventados**. Si falta informacion, declarala explicitamente.
3. **Distinguir evidencia de inferencia**. Usa frases como "Segun el codigo leido en..." o "No encontre evidencia de...".
4. **No proponer soluciones genericas sin calzarlas al repo**. Preferi adaptar el codigo existente antes de importar un patron nuevo.

## Ejemplos de alucinaciones y correcciones

### 1. Inventar funciones o parametros

**Incorrecto:**
> "La funcion `validateCard()` ya recibe un segundo parametro `userId`."

**Correcto:**
> "No encontre la funcion `validateCard()` en el codigo leido. Necesito buscarla antes de afirmar su firma."

### 2. Agregar dependencias sin verificar

**Incorrecto:**
> "Vamos a usar `jackson-databind` 2.15 para serializar el DTO."

**Correcto:**
> "Verifico `pom.xml` para confirmar si `jackson-databind` ya esta declarado y en que version."

### 3. Asumir el stack

**Incorrecto:**
> "Como veo `package.json`, esto es un proyecto NestJS."

**Correcto:**
> "Veo un `package.json`; necesito verificar si contiene `@nestjs/core` u otro framework antes de aplicar un perfil."

### 4. Inventar comandos de validacion

**Incorrecto:**
> "Ejecuta `npm run test:ci` para validar."

**Correcto:**
> "Reviso los scripts definidos en `package.json` y uso el comando de test que el proyecto tenga configurado."

### 5. Proponer cambios fuera del alcance

**Incorrecto:**
> "Aprovecho para migrar toda la capa de persistencia a JPA."

**Correcto:**
> "Me limito a la tarea solicitada. Si detecto algo fuera de alcance, lo reporto como hallazgo sin modificarlo."

## Senales de que estas alucinando

- Usas una ruta de archivo que no leiste.
- Mencionas un nombre de clase o funcion sin haberlo encontrado con `grep_search` o `code_search`.
- Propones una libreria o version por "costumbre" sin revisar el manifiesto de dependencias.
- Respondes con certeza absoluta sobre un archivo que no se te proporciono.
- Introduces cambios en multiples capas sin que la tarea lo pida.

## Frases permitidas para declarar incertidumbre

- "No encontre..."
- "No pude verificar..."
- "Esto depende de..."
- "Necesito mas contexto para..."
- "Segun los archivos que lei, ..."

## Checklist antes de responder

- [ ] Lei los archivos relevantes con `read_file`.
- [ ] Busque codigo similar con `grep_search` o `code_search`.
- [ ] Verifique las dependencias y versiones en el manifiesto correspondiente.
- [ ] Ejecute o propuse ejecutar el comando de validacion del perfil.
- [ ] Toda cita de archivo incluye ruta absoluta y rango de lineas.
- [ ] Si no estoy seguro, lo declare explicitamente.
