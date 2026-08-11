# devin-agents

Biblioteca centralizada de agentes de IA especializados para acompañar el desarrollo de software: backend, testing, DevOps y QA.

## Objetivo

Proporcionar prompts, perfiles de stack y conocimiento compartido que cualquier proyecto pueda consumir. Los agentes detectan el stack del repositorio y aplican las reglas y buenas practicas correspondientes.

## Estructura

- `prompts/`: system prompts base y especializados por rol.
- `profiles/`: configuraciones especificas por stack tecnologico.
- `knowledge/`: guias de arquitectura, testing y errores comunes.
- `examples/`: ejemplos de interacciones para calibrar respuestas.
- `config/default.yaml`: configuracion por defecto.

## Como usarlo en un proyecto

### Opcion 1: git submodule

```bash
git submodule add https://github.com/<tu-cuenta>/devin-agents.git .agents/shared
git submodule update --init
```

### Opcion 2: referencia remota

Agregar en la raiz del proyecto:

```yaml
# .ai-agents.yaml
agents_repo: https://github.com/<tu-cuenta>/devin-agents
profile: java-spring-boot
agents:
  - backend
  - testing
  - devops
  - qa
```

### Opcion 3: clonar manualmente

```bash
git clone https://github.com/<tu-cuenta>/devin-agents.git ~/.devin-agents
```

## Como agregar un perfil de stack

1. Crear `profiles/<stack>.md`.
2. Describir lenguaje, framework, build tool, test framework, comandos de validacion y convenciones.
3. Referenciarlo desde `.ai-agents.yaml` del proyecto.

## Seguridad

- No incluir secretos, tokens ni credenciales en los prompts.
- Si los prompts contienen informacion sensible de arquitectura, mantener el repo privado y con acceso restringido.
