# Guia de Estudio para Certificacion APX - BBVA

## Que es APX

**APX (Arquitectura Plataforma Extendida)** es una plataforma interna y propietaria de BBVA para el desarrollo de aplicaciones backend transaccionales basadas en Java. Se divide en dos modos operativos:

- **Online**: procesamiento sincrono de transacciones
- **Batch**: procesamiento asincrono/masivo

APX fue creada como extension del mainframe (host) con el objetivo de reducir su uso y desacoplar la logica de negocio.

### Relacion con ASO y Ether

- **ASO (Arquitectura de Sistemas Orientada a Servicios)**: se enfoca en servicios individuales reutilizables
- **APX**: orquesta procesos de negocio completos
- **Ether**: ecosistema integral que contiene **Cells** (frontend) + **APX** (backend) + bases de datos (Alpha/DDBB)

En 2019 el 67% de los modelos de solucion utilizaron Ether (83 de 124 soluciones). BBVA tenia 524 servicios ASO productivos (49% globales, 37% de reutilizacion).

---

## Stack Tecnologico

| Categoria | Tecnologia |
|-----------|-----------|
| Lenguajes | Java 8 (minimo), Java 11+ |
| Frameworks | Spring Framework, Spring Boot, Spring Batch (batch) |
| Build | Maven (pom) |
| Contenedor OSGi | Apache Felix (bundles modulares) |
| Logging | Log4j |
| IDE | Eclipse |
| Testing de API | Postman |
| Control de versiones | Bitbucket / Git |
| CLI | APX CLI (ej. `apx add util -n jdbc -y`) |
| Calidad | SonarQube, tests unitarios (75-80% cobertura minima) |
| CI/CD | Jenkins + GitLab |
| Despliegue | .jar / .zip |
| Bases de datos | Oracle, MongoDB, ElasticSearch |
| Scheduling | Control-M (jobs batch) |
| Monitoreo | Atenea, Monitor APX, Consola de Operaciones APX, Kibana |
| Infraestructura | Red Hat OpenShift sobre OpenStack (IaaS), contenedores |

---

## Arquitectura Detallada

### Capas

- **Capa de Control**: recibe informacion, despacha ejecucion de transacciones, crea contexto transaccional (session), provee scope transaccional para commit/rollback, gestiona pre/post acciones
- **Capa de Negocio**: logica de negocio encapsulada en microservicios Java
- **Capa de Datos**: acceso a datos exclusivamente via la implementacion (Implementation es el unico componente con acceso directo a BD)

### Componentes Online

- **Transaction**: unidad de ejecucion principal
- **Library**: logica reutilizable (tipos: Simple, Complex, Rule Engine)
- **DTO (Data Transfer Object)**: objetos de transferencia de datos

### Conectores

| Conector | Uso |
|----------|-----|
| **JDBC Connector** | Acceso a bases de datos relacionales |
| **API Connector** | Invocacion de APIs REST externas/internas |
| **Kafka Connector** | Publicacion/suscripcion de eventos |
| **SOAP Connector** | Servicios legacy XML |
| **IMS Connector** | Acceso al mainframe (Host) via Interbackend Proxy |

### Utilidades comunes (Online y Batch)

- **Communication Manager**: libreria para invocar G.U. y enviar notificaciones
- **Interbackend Proxy**: libreria para invocar IMS Connectors para acceso al Host

---

## Reglas y Restricciones Criticas

| Regla | Detalle |
|-------|---------|
| Profundidad maxima de invocacion | 3 niveles (Transaction > Library > Library > Library) |
| Invocacion sincrona entre transacciones | **PROHIBIDA** (previene deadlocks) |
| Zonas de ejecucion asincrona | Zona 20 y Zona A0 |
| Nomenclatura de proyectos | `[UUAA][codigo][version]` donde UUAA = Unidad Funcional (4 caracteres) |
| Codigos de transaccion | 4 caracteres, inician con T |
| Codigos UUAA | 4 caracteres |

---

## Ambientes de Despliegue

Orden obligatorio:

```
Desarrollo → Integrado → AUS → Octa → Produccion
```

### Ventanas de despliegue

- 05:30 UTC
- 06:30 UTC
- 15:30 UTC
- 19:30 UTC

---

## Branching

| Tipo de branch | Destino |
|---------------|---------|
| **Feature** | Solo a desarrollo |
| **Release** | Llega a produccion |
| **Hotfix** | Derivan de release candidates |

---

## Manejo de Errores

- `addAdvice()`: advertencias al stack
- `setSeverity()`: nivel de criticidad

### Excepciones capturables

- `IOException`
- `DataIntegrityViolationException`
- `RestClientException`

### Excepciones NO capturables

- `TimeOutException`

---

## Seguridad en APX

- Uso de **vaults** para secretos (nunca hardcoded)
- Validacion de inputs
- Prohibicion de conexiones directas al mainframe
- Alineacion con practicas **OWASP**

---

## Monitoreo

| Herramienta | Funcion |
|------------|---------|
| Atenea | Monitoreo general |
| Monitor APX | Monitoreo de transacciones APX |
| Consola de Operaciones APX | Gestion operativa |
| Kibana | Visualizacion de logs |
| Control-M | Scheduling de jobs batch |

---

## Anti-patrones

- **Blob**: clase con funcionalidad excesiva
- **Magic Container**: un metodo ejecutando multiples operaciones por filtro

---

## Infraestructura Cloud BBVA

- **IaaS/PaaS**: Red Hat OpenShift sobre OpenStack
- **API Gateway**: Broadcom Layer 7 Suite (API Gateway + API Portal)
- **Seguridad API**: OAuth 2.0
- **Orquestacion**: Kubernetes
- **Plataforma de datos**: ADA (Analytics + Data + AI) sobre AWS

---

## Temas Mas Preguntados en el Examen

Basado en tests de Daypo y flashcards de Quizlet:

1. Componentes Online (Transaction, Library, DTO)
2. Conectores (JDBC, API, Kafka, SOAP, IMS)
3. Nomenclatura (UUAA, codigos de transaccion)
4. Ambientes de despliegue y su orden
5. Ventanas de despliegue
6. Profundidad maxima de invocacion (3 niveles)
7. Prohibicion de invocacion sincrona entre transacciones
8. Manejo de errores (addAdvice, setSeverity, excepciones)
9. Branching (Feature, Release, Hotfix)
10. Seguridad (vaults, validacion, OWASP)
11. Batch (Spring Batch, Control-M, zonas 20/A0)
12. Monitoreo (Atenea, Kibana, Monitor APX)

---

## Recursos de Estudio

### Examenes de practica (Daypo) — GRATIS, sin registro

| Recurso | URL |
|---------|-----|
| Examen Certificacion APX 1 | https://www.daypo.com/examen-certificacion-apx-1.html |
| Examen Certificacion APX 2 | https://www.daypo.com/examen-certificacion-apx-2.html |
| Test APX (74 preguntas con respuestas) | https://www.daypo.com/880084.html |
| Test APX adicional | https://www.daypo.com/188740.html |
| Test Compartido APX | https://www.daypo.com/compartido-apx.html |

### Flashcards (Quizlet) — GRATIS

| Recurso | URL |
|---------|-----|
| Certificacion APX (Mexico) | https://quizlet.com/mx/832904227/certificacion-apx-flash-cards/ |
| Certificacion APX (Espana) | https://quizlet.com/es/779789495/certificacion-apx-flash-cards/ |
| APX - 191 terminos | https://quizlet.com/mx/936253481/apx-flash-cards/ |
| APX Guia Mentor 1-100 (100 preguntas) | https://quizlet.com/mx/939030431/apx-guia-mentor-1-100-flash-cards/ |
| Consola APX Batch | https://quizlet.com/mx/696653868/consola-apx-batch-flash-cards/ |
| APX Flashcards | https://quizlet.com/mx/578295960/apx-flash-cards/ |
| APX Flashcards | https://quizlet.com/mx/927807674/apx-flash-cards/ |
| Vision General APX | https://quizlet.com/mx/600898205/vision-general-flash-cards/ |
| APX Quiz | https://quizlet.com/583147524/apx-quiz-flash-cards/ |

### Guias teoricas y examenes (Studocu) — Requiere registro gratuito

| Recurso | URL |
|---------|-----|
| Guia Teorica y Tecnica para Certificacion APX | https://www.studocu.com/es-mx/document/universidad-sabes-san-jose-iturbide/tecnologias-de-la-informacion/guia-teorica-y-tecnica-para-certificacion-apx-bbva-introduccion-y-componentes/129492914 |
| Examen APX Teoria 2021 - Preguntas y Respuestas | https://www.studocu.com/es-mx/document/universidad-sabes-san-jose-iturbide/tecnologias-de-la-informacion/guia-examen-apx-teoria-2021-preguntas-y-respuestas-clave/129492776 |
| Examen APX Teoria 2021 Julio (UNAM) | https://www.studocu.com/es-mx/document/universidad-nacional-autonoma-de-mexico/programacion-de-matlab/guia-examen-apx-teoria-2021-julio/89030706 |
| Examen APX Java 2021 - Preguntas y Respuestas | https://www.studocu.com/es-mx/document/universidad-nacional-autonoma-de-mexico/programacion-de-matlab/guia-examen-apx-java-2021-julio/89030709 |
| Guia APX Teoria 3 - Desarrollo Seguro | https://www.studocu.com/es-mx/document/universidad-madero/ingenieria-calidad/guia-apx-teoria-3-guias-para-desarrollo-seguro-de-software/42367365 |
| Examen Final APX - Respuestas | https://www.studocu.com/es-mx/document/zona-escolar-gustavo-a-madero-07264-mexico-city-cdmx-mexico/analisis-proyectual/respuestas-apx-1-dfcvg/111591907 |
| Arquitecturas Extendidas APX | https://www.studocu.com/es-mx/document/universidad-autonoma-del-estado-de-mexico/arquitectura-de-computadoras/info-de-arquitecturas-extendidas/114639650 |
| APX Resumen para Exposicion (IPN) | https://www.studocu.com/es-mx/document/centro-de-estudios-cientificos-y-tecnologicos-n0-1-gonzalo-vazquez-vela-ipn/sistema-de-informacion/tecnologia-apx-de-bbva-resumen-para-exposicion-en-clase/144912183 |
| Guia APX Material de Apoyo | https://www.studocu.com/es-mx/document/universidad-nacional-autonoma-de-mexico/programacion/guia-material-de-apoyo/119695827 |
| Examen APX Teoria 2021 (UT El Retono) | https://www.studocu.com/es-mx/document/universidad-tecnologica-el-retono/taller-de-investigacion/guia-examen-apx-teoria-2021-julio/103349693 |

### Presentaciones y articulos

| Recurso | URL |
|---------|-----|
| Presentacion APX (Prezi - Victor Garcia) | https://prezi.com/p/8tvghjjmjjez/apx/ |
| Presentacion APX (Prezi - Juan Carlos Valencia) | https://prezi.com/p/isnq42vzgnbp/apx/ |
| Que son ASO y APX (articulo) | https://localhorse.net/article/que-son-las-arquitecturas-aso-y-apx |
| APX BBVA Plataforma tecnologica (blog) | https://alzado.org/2020/05/25/apx-bbva-plataforma-tecnolgica-del-bbva/ |
| Quiz interactivo Arquitectura APX (Wordwall) | https://wordwall.net/resource/55522543/arquitectura-apx |

### Codigo fuente (GitHub)

| Recurso | URL |
|---------|-----|
| Curso Java APX (codigo real) | https://github.com/LyanRoy/CursoJavaAPX |
| Laboratorio APX BBVA (setup IDE) | https://github.com/wildrakbil/apx-laboratory-bbva |
| Open Cells - frontend Ether (BBVA oficial) | https://github.com/BBVA/open-cells |

### Otros recursos

| Recurso | URL |
|---------|-----|
| Academia BBVA APX (Softtek/Quia) | https://www.quia.com/pages/softtekuniversity/page436 |
| APX Introduccion Plataforma PDF (CourseHero, requiere suscripcion) | https://www.coursehero.com/file/57458745/Mr5Minutes-APX-Introduccion-Plataformapdf/ |
| Guia de Despliegue APX (Scribd) | https://www.scribd.com/document/687114314/Comandos-Batch-Bien-Hechos |
| BBVA Memoria 2019 Engineering | https://extranetperu.grupobbva.pe/memoria2019/engineering.html |
| Guia de uso BBVA (Scribd) | https://www.scribd.com/document/817034199/Guia-de-uso-bbva |

### Documentacion interna BBVA (requiere credenciales @bbva.com)

| Recurso | URL |
|---------|-----|
| Wiki oficial APX Plataforma Extendida | https://sites.google.com/a/bbva.com/apx-plataforma-extendida/ |

### Conferencias y presentaciones tecnicas BBVA

| Recurso | URL |
|---------|-----|
| APIdays Zurich 2019 - BBVA API Market (SlideShare) | https://www.slideshare.net/slideshow/apidays-zurich-2019-the-experience-of-bbva-api-market-david-ramos-lehnhoff-bbva/148808520 |
| APIdays Paris 2025 - API Layer7 Security BBVA (SpeakerDeck) | https://speakerdeck.com/apidays/apidays-paris-2025-api-layer7-security-real-world-use-cases-bbva-and-nexi |
| BBVA DevSecOps - Rooted 2018 (SlideShare) | https://www.slideshare.net/slideshow/ernesto-bethencourt-javier-sanz-ofreciendo-seguridad-de-autoconsumo-a-los-desarrolladores-para-escalar-a-una-cultura-devsecops/90442165 |
| Red Hat + BBVA OpenShift | https://www.redhat.com/de/blog/red-hat-openshift-red-hat-openstack-platform-flexibility-key-bbvas-digital-transformation |
| BBVA + AWS Data Platform | https://aws.amazon.com/blogs/industries/part-1-bbva-building-a-multi-region-multi-country-global-data-and-ml-platform-at-scale/ |

### Entrevistas y vacantes (revelan temas tecnicos)

| Recurso | URL |
|---------|-----|
| Preguntas de entrevista BBVA (Glassdoor) | https://www.glassdoor.com/Interview/BBVA-Interview-Questions-E1237.htm |
| BBVA Next Technologies entrevistas (Glassdoor) | https://www.glassdoor.com/Interview/BBVA-Next-Technologies-Interview-Questions-E3138800.htm |
| Vacante Desarrollador APX (LinkedIn) | https://mx.linkedin.com/jobs/view/desarrollador-apx-miguel-hidalgo-cdmx-at-bbva-4128284782 |
| Desarrolladores APX-ASO (Tecnoempleo) | https://www.tecnoempleo.com/desarrolladores-apx-aso-hibrido/aso-apx/rf-78781d0d7262434b904d |
| Empleos APX (Indeed Mexico) | https://mx.indeed.com/q-desarrollador-apx-empleos.html |

---

## Plan de Estudio Sugerido (tiempo limitado)

1. **Primero**: Hacer los 5 tests de Daypo (gratuitos, sin registro) para conocer formato y temas del examen
2. **Segundo**: Estudiar los flashcards de Quizlet (especialmente "Guia Mentor 1-100" y "Certificacion APX")
3. **Tercero**: Registrarse en Studocu y descargar las guias teoricas y examenes con respuestas
4. **Cuarto**: Revisar las presentaciones de Prezi y el articulo de localhorse.net para entender la arquitectura general
5. **Quinto**: Explorar el codigo en GitHub (CursoJavaAPX) para ver la estructura real de proyectos APX
