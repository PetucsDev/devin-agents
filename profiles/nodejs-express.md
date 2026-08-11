# Perfil: Node.js Express

## Stack

- Lenguaje: JavaScript / TypeScript
- Framework: Express.js
- Build tool: npm / yarn / pnpm
- Tests: Jest, Mocha, Chai, Supertest
- Persistencia: segun el proyecto (mongoose, sequelize, pg, etc.)
- Contenedores: Docker

## Deteccion

Se activa con `package.json` que contenga `express` y no contenga `@nestjs/core`.

## Comandos de validacion

- Instalar dependencias: `npm install`
- Tests: `npm test`
- Lint: `npm run lint`
- Type check (si aplica TypeScript): `npm run build` o `tsc --noEmit`

## Archivos de verificacion obligatoria

Antes de proponer cambios, lee y considera:

- `README.md` y `.ai-agents.yaml`.
- `package.json` (scripts, version de Express, dependencias de testing).
- `tsconfig.json` si el proyecto usa TypeScript.
- Estructura bajo `src/` o `routes/`.
- Middleware de manejo de errores existente.
- No inventes routers, middlewares, modelos ni dependencias que no aparezcan en estos archivos.

## Convenciones

- Rutas en `routes/`, controladores en `controllers/`, logica de negocio en `services/`.
- Middleware reutilizable para validacion, autenticacion y manejo de errores.
- Uso de `express-async-errors` o wrapper para capturar errores asincronicos.
- Tests de endpoints con `supertest`.

## Anti-patrones a evitar

- Logica de negocio en handlers de rutas.
- Uso extensivo de `any` en TypeScript.
- Manejo de errores con `res.status(500).send(err)` sin normalizar.
- Callbacks sin manejo de errores.
- Dependencias globales mutables.
