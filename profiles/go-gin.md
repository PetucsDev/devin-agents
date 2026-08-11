# Perfil: Go Gin

## Stack

- Lenguaje: Go 1.21+
- Framework: Gin
- Build tool: go modules
- Tests: testing estandar + testify
- Persistencia: segun el proyecto
- Contenedores: Docker

## Deteccion

Se activa con `go.mod` que contenga `github.com/gin-gonic/gin`.

## Comandos de validacion

- Tests: `go test ./...`
- Build: `go build ./...`
- Lint: `golangci-lint run`
- Format: `gofmt -w .`

## Archivos de verificacion obligatoria

Antes de proponer cambios, lee y considera:

- `README.md` y `.ai-agents.yaml`.
- `go.mod` y `go.sum` (version de Go, dependencias).
- Entrypoint principal (`main.go`, `cmd/`).
- Estructura de paquetes y `_test.go` existentes.
- No inventes handlers, servicios, tipos ni dependencias que no aparezcan en estos archivos.

## Convenciones

- Handlers delegan a servicios.
- Modelos separados de DTOs.
- Manejo de errores explicito.
- Tests en archivos `_test.go` en el mismo paquete.

## Anti-patrones a evitar

- Logica de negocio en handlers.
- Panic sin recover.
- Imports no utilizados.
