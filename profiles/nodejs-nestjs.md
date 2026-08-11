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

## Convenciones

- Modulos, controladores y servicios con la estructura de NestJS.
- DTOs validados con `class-validator`.
- Inyeccion de dependencias nativa de NestJS.
- Tests unitarios con Jest, mocks con `jest.mock`.

## Anti-patrones a evitar

- Logica de negocio en controladores.
- Imports circulares entre modulos.
- Uso de `any` extensivo.
