# Perfil: Java Spring Boot

## Stack

- Lenguaje: Java 17+
- Framework: Spring Boot
- Build tool: Maven (`pom.xml`) o Gradle (`build.gradle`)
- Tests: JUnit 5, Mockito, AssertJ, Spring Boot Test, Testcontainers
- Persistencia: JPA / Hibernate, PostgreSQL
- Mensajeria: Kafka (opcional)
- Contenedores: Docker
- Infra: Kubernetes, Terraform (opcional)

## Deteccion

Este perfil se activa si existe `pom.xml` o `build.gradle` con dependencias de Spring Boot.

## Comandos de validacion

- Compilar y testear: `mvn clean verify`
- Solo tests: `mvn test`
- Tests de integracion: `mvn failsafe:integration-test`
- Build de imagen: `docker build -t <imagen> .`
- Terraform: `terraform plan` dentro de la carpeta de infra correspondiente.

## Convenciones

- Estructura de paquetes por feature o por capa, segun el proyecto.
- DTOs en `api.dto`, entidades en `domain` o `repository.entity`.
- Servicios anotados con `@Service` y `@Transactional` cuando corresponda.
- Inyeccion de dependencias por constructor.
- Tests unitarios terminan en `Test`.
- Tests de integracion terminan en `IntegrationTest` y se ejecutan con Failsafe.

## Anti-patrones a evitar

- `@Autowired` en campos. Preferir inyeccion por constructor.
- Logica de negocio en controladores.
- Consultas N+1 sin `fetch` adecuado.
- Tests que dependen del orden de ejecucion.
