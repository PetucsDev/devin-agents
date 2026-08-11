# Perfil: Node.js NestJS

## Stack

- Lenguaje: TypeScript / JavaScript
- Framework: NestJS
- Build tool: npm / yarn / pnpm
- Tests: Jest
- Persistencia: TypeORM, Prisma o Mongoose (segun el proyecto)
- Contenedores: Docker
- Infra: Kubernetes, Terraform (opcional)

## Deteccion

Se activa con `package.json` que contenga `@nestjs/core`.

## Comandos de validacion

- Instalar dependencias: `npm install`
- Tests: `npm test`
- Build: `npm run build`
- Lint: `npm run lint`
- Si el proyecto usa scripts custom (ej. `test:integration`, `test:e2e`), usalos segun `package.json`.

## Archivos de verificacion obligatoria

Antes de proponer cambios, lee y considera:

- `README.md` y `.ai-agents.yaml`.
- `package.json` (scripts, versiones de NestJS, dependencias de testing).
- `tsconfig.json`.
- Configuracion de Jest (`jest.config.js`, `jest` en `package.json` o archivos de preset).
- Estructura bajo `src/`.
- No inventes modulos, providers ni nombres de dependencias que no aparezcan en estos archivos.

## Convenciones

- Modulos, controladores y servicios con la estructura de NestJS.
- DTOs validados con `class-validator`.
- Inyeccion de dependencias nativa de NestJS.
- Tests unitarios con Jest, mocks con `jest.mock`.

## Anti-patrones a evitar

- Logica de negocio en controladores.
- Imports circulares entre modulos.
- Uso de `any` extensivo.
