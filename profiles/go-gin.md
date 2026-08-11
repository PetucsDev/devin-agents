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

## Convenciones

- Handlers delegan a servicios.
- Modelos separados de DTOs.
- Manejo de errores explicito.
- Tests en archivos `_test.go` en el mismo paquete.

## Anti-patrones a evitar

- Logica de negocio en handlers.
- Panic sin recover.
- Imports no utilizados.
