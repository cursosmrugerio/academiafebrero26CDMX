# JUnit 5 - Primer contacto con testing

## Que es testing y por que importa

Imagina que compras un carro nuevo. Antes de manejarlo en la carretera, haces un test drive: arrancas el motor, pruebas los frenos, giras el volante, verificas que las luces funcionan. No conducirias un carro sin haberlo probado primero.

El testing de software es exactamente eso: **verificar que el codigo funciona correctamente antes de usarlo en produccion**. En lugar de probar manualmente cada vez (abrir Postman, enviar un request, revisar la respuesta...), escribimos codigo que prueba nuestro codigo de forma automatica.

Ventajas del testing automatizado:

| Sin tests | Con tests |
|-----------|-----------|
| Pruebas manuales cada vez que cambias algo | Ejecutas `mvn test` y en 2 segundos sabes si algo se rompio |
| "Funciona en mi maquina" | Funciona en cualquier maquina que corra los tests |
| Miedo de tocar codigo existente | Confianza para refactorizar: los tests te avisan si rompiste algo |
| Errores se descubren en produccion | Errores se descubren al escribir el codigo |

**JUnit 5** es el framework de testing estandar de Java. Viene incluido en cualquier proyecto Spring Boot.

---

## Que hay de nuevo en este proyecto

Este proyecto es la misma API REST de alumnos con MongoDB que ya conoces, pero ahora incluye **tests unitarios**. La aplicacion (entidad, servicio, controlador, repositorio) no cambio — solo se agregaron archivos de test.

### Archivos nuevos (test)

| Archivo | Que prueba | Tests |
|---------|-----------|-------|
| `src/test/.../entity/AlumnoTest.java` | La entidad Alumno: constructor, getters, setters | 8 |
| `src/test/.../service/AlumnoServiceTest.java` | El servicio AlumnoService: CRUD completo | 12 |
| `src/test/.../fake/FakeAlumnoRepository.java` | Implementacion falsa del repositorio (no es un test, es una herramienta para los tests) | — |

### Archivos existentes (no cambian)

| Archivo | Rol |
|---------|-----|
| `src/main/.../entity/Alumno.java` | Entidad/modelo |
| `src/main/.../repository/AlumnoRepository.java` | Interface del repositorio (extiende MongoRepository) |
| `src/main/.../service/AlumnoService.java` | Logica de negocio |
| `src/main/.../controller/AlumnoController.java` | Endpoints REST |

**Total: 20 tests, todos pasan.**

---

## Anatomia de un test

Un test en JUnit 5 es un metodo con la anotacion `@Test`. Veamos el ejemplo mas simple del proyecto:

```java
@Test
@DisplayName("setNombre y getNombre guardan y devuelven el nombre")
void setNombre_valorValido_retornaMismoValor() {
    // Arrange - preparar los datos
    Alumno alumno = new Alumno();

    // Act - ejecutar la accion que queremos probar
    alumno.setNombre("Juan");

    // Assert - verificar que el resultado es el esperado
    assertEquals("Juan", alumno.getNombre());
}
```

### Las 3 partes de un test (patron AAA)

| Paso | Que hace | En el ejemplo |
|------|---------|---------------|
| **Arrange** (preparar) | Crear los objetos y datos necesarios | `new Alumno()` |
| **Act** (ejecutar) | Llamar al metodo que estamos probando | `setNombre("Juan")` |
| **Assert** (verificar) | Comprobar que el resultado es correcto | `assertEquals("Juan", ...)` |

### Las anotaciones clave

| Anotacion | Para que sirve |
|-----------|---------------|
| `@Test` | Marca el metodo como un test. JUnit lo ejecuta automaticamente |
| `@DisplayName("...")` | Nombre descriptivo que aparece en el reporte de tests |
| `@BeforeEach` | Metodo que se ejecuta **antes de cada test** (para preparar estado fresco) |

---

## Aserciones basicas

Las aserciones son los metodos que usamos en el paso Assert para verificar resultados. Todas vienen de `org.junit.jupiter.api.Assertions`.

| Asercion | Que verifica | Ejemplo del proyecto |
|----------|-------------|---------------------|
| `assertEquals(esperado, actual)` | Que dos valores sean iguales | `assertEquals("Juan", alumno.getNombre())` |
| `assertNull(valor)` | Que el valor sea `null` | `assertNull(alumno.getId(), "id debe ser null")` |
| `assertNotNull(valor)` | Que el valor NO sea `null` | `assertNotNull(resultado.getId(), "Debe generar un ID")` |
| `assertTrue(condicion)` | Que la condicion sea `true` | `assertTrue(resultado.isPresent(), "Debe encontrar al alumno")` |
| `assertFalse(condicion)` | Que la condicion sea `false` | `assertFalse(resultado, "Debe retornar false si no existe")` |
| `assertAll(nombre, lambdas...)` | Ejecuta TODAS las verificaciones aunque alguna falle | Ver ejemplo abajo |

### assertAll: verificar multiples cosas a la vez

Sin `assertAll`, si la primera asercion falla, las demas no se ejecutan:

```java
// Si esta falla, las siguientes NO se ejecutan
assertEquals("xyz789", alumno.getId());
assertEquals("Maria", alumno.getNombre());     // nunca se verifica
assertEquals("Lopez", alumno.getApellido());   // nunca se verifica
```

Con `assertAll`, TODAS se ejecutan y el reporte muestra todas las que fallaron:

```java
// Del AlumnoTest.java:
assertAll("Propiedades del alumno",
    () -> assertEquals("xyz789", alumno.getId()),
    () -> assertEquals("Maria", alumno.getNombre()),
    () -> assertEquals("Lopez", alumno.getApellido()),
    () -> assertEquals("maria@correo.com", alumno.getEmail()),
    () -> assertEquals(LocalDate.of(2026, 1, 15), alumno.getFechaRegistro())
);
```

Cada lambda `() -> ...` es una verificacion independiente. Si una falla, las demas siguen ejecutandose. Esto es util cuando pruebas un objeto con multiples propiedades — quieres saber **todo** lo que esta mal, no solo lo primero.

### El segundo parametro (mensaje)

Todas las aserciones aceptan un mensaje opcional como ultimo parametro. Este mensaje aparece cuando el test falla, para ayudarte a entender que salio mal:

```java
assertNull(alumno.getId(), "id debe ser null");
assertTrue(resultado.isEmpty(), "No debe encontrar al alumno");
assertEquals(2, resultado.size(), "Debe haber 2 alumnos");
```

---

## @BeforeEach: estado fresco para cada test

Cuando probamos un servicio, cada test necesita un estado limpio. Si un test inserta un alumno y otro test espera una lista vacia, se interfieren entre si. `@BeforeEach` resuelve esto:

```java
// Del AlumnoServiceTest.java:
class AlumnoServiceTest {

    private AlumnoService service;
    private FakeAlumnoRepository fakeRepository;

    @BeforeEach
    void setUp() {
        // Antes de cada test, creamos un fake limpio y un servicio nuevo
        // Esto garantiza que los tests son independientes entre si
        fakeRepository = new FakeAlumnoRepository();
        service = new AlumnoService(fakeRepository);
    }

    @Test
    void listarTodos_sinAlumnos_retornaListaVacia() {
        // El repositorio ya esta vacio gracias al setUp
        List<Alumno> resultado = service.listarTodos();
        assertTrue(resultado.isEmpty());
    }

    @Test
    void listarTodos_conAlumnos_retornaTodos() {
        // Otro repositorio vacio — no le afecta el test anterior
        service.crear(crearAlumno("Juan", "Perez", "juan@correo.com"));
        service.crear(crearAlumno("Maria", "Lopez", "maria@correo.com"));
        assertEquals(2, service.listarTodos().size());
    }
}
```

Flujo de ejecucion:

```
setUp()  →  test 1 (repositorio vacio)
setUp()  →  test 2 (repositorio vacio de nuevo)
setUp()  →  test 3 (repositorio vacio de nuevo)
...
```

Cada test arranca con un `FakeAlumnoRepository` nuevo (HashMap vacio) y un `AlumnoService` nuevo. No importa en que orden se ejecuten los tests ni cuantos alumnos inserto el test anterior.

---

## El FakeAlumnoRepository

Este es el archivo mas interesante del proyecto desde el punto de vista educativo. El problema es el siguiente:

`AlumnoService` depende de `AlumnoRepository` para funcionar. Pero `AlumnoRepository` es una interface de Spring Data que necesita MongoDB para funcionar. Si queremos probar el servicio **sin levantar Spring ni MongoDB**, necesitamos una implementacion falsa.

### Diagrama de la relacion

```
En produccion (con Spring):

  AlumnoService  ──usa──>  AlumnoRepository  ──implementa──>  Spring Data + MongoDB
                           (interface)

En tests (sin Spring):

  AlumnoService  ──usa──>  AlumnoRepository  ──implementa──>  FakeAlumnoRepository
                           (interface)                         (HashMap en memoria)
```

El servicio no sabe (ni le importa) si habla con MongoDB o con un HashMap. Solo sabe que tiene un objeto que cumple el contrato de `AlumnoRepository`.

### Como funciona el fake

```java
public class FakeAlumnoRepository implements AlumnoRepository {

    // En lugar de MongoDB, usamos un HashMap
    private final Map<String, Alumno> datos = new HashMap<>();

    // Solo implementamos los 5 metodos que AlumnoService realmente usa:

    @Override
    public List<Alumno> findAll() {
        return new ArrayList<>(datos.values());
    }

    @Override
    public Optional<Alumno> findById(String id) {
        return Optional.ofNullable(datos.get(id));
    }

    @Override
    public <S extends Alumno> S save(S alumno) {
        if (alumno.getId() == null) {
            alumno.setId(UUID.randomUUID().toString());
        }
        datos.put(alumno.getId(), alumno);
        return alumno;
    }

    @Override
    public boolean existsById(String id) {
        return datos.containsKey(id);
    }

    @Override
    public void deleteById(String id) {
        datos.remove(id);
    }

    // Los otros 18 metodos heredados lanzan UnsupportedOperationException
    // porque AlumnoService nunca los llama
}
```

### El problema que esto ilustra

`MongoRepository` hereda de `ListCrudRepository`, `ListPagingAndSortingRepository` y `QueryByExampleExecutor`. En total, `FakeAlumnoRepository` tiene que declarar **23 metodos**, pero solo usa 5. Los otros 18 son:

```java
@Override
public <S extends Alumno> List<S> saveAll(Iterable<S> entities) {
    throw new UnsupportedOperationException("No implementado en el fake");
}

// ... y 17 metodos mas iguales
```

**Este es exactamente el problema que resuelve Mockito** (que veremos en el siguiente proyecto): crear implementaciones falsas de interfaces grandes de forma automatica, sin escribir 18 metodos que solo dicen "no implementado".

---

## Recorrido por los tests

### AlumnoTest (8 tests) — probar la entidad

Este archivo prueba la entidad `Alumno` de forma aislada. No necesita servicio, repositorio ni base de datos. Solo crea objetos `Alumno` y verifica que los getters/setters funcionan.

**Test 1: Constructor vacio**
```java
@Test
@DisplayName("Constructor vacio crea alumno con campos nulos")
void constructorVacio_sinParametros_camposNulos() {
    Alumno alumno = new Alumno();

    assertAll("Estado inicial del alumno",
        () -> assertNull(alumno.getId()),
        () -> assertNull(alumno.getNombre()),
        () -> assertNull(alumno.getApellido()),
        () -> assertNull(alumno.getEmail()),
        () -> assertNull(alumno.getFechaRegistro())
    );
}
```

Verifica que un alumno recien creado tiene todos sus campos en `null`. Usa `assertAll` para verificar los 5 campos de una sola vez.

**Tests 2 a 5: Getters y setters individuales**

Cada test verifica un par getter/setter: `setNombre`/`getNombre`, `setApellido`/`getApellido`, `setEmail`/`getEmail`, `setId`/`getId`. Son tests simples con patron AAA puro.

**Tests 6 y 7: LocalDate**

```java
@Test
@DisplayName("setFechaRegistro guarda la fecha correctamente")
void setFechaRegistro_fechaValida_retornaMismaFecha() {
    Alumno alumno = new Alumno();
    LocalDate fecha = LocalDate.of(2026, 2, 24);

    alumno.setFechaRegistro(fecha);

    assertEquals(fecha, alumno.getFechaRegistro());
}
```

Demuestran que `assertEquals` funciona con cualquier tipo que implemente `equals()`, no solo con `String` y numeros. `LocalDate` es un buen ejemplo porque es inmutable y tiene `equals` bien definido.

**Test 8: assertAll con todas las propiedades**

Crea un alumno completo (con todos los campos) y verifica todo con `assertAll`. Es el test mas completo de la entidad.

### AlumnoServiceTest (12 tests) — probar la logica de negocio

Este archivo prueba `AlumnoService` usando el `FakeAlumnoRepository`. Cubre las 5 operaciones CRUD del servicio.

**listarTodos (2 tests)**

| Test | Escenario | Asercion clave |
|------|----------|---------------|
| `listarTodos_sinAlumnos_retornaListaVacia` | Sin datos | `assertTrue(resultado.isEmpty())` |
| `listarTodos_conAlumnos_retornaTodos` | Con 2 alumnos insertados | `assertEquals(2, resultado.size())` |

**buscarPorId (2 tests)**

| Test | Escenario | Asercion clave |
|------|----------|---------------|
| `buscarPorId_alumnoExiste_retornaAlumno` | ID que existe | `assertTrue(resultado.isPresent())` + verificar nombre |
| `buscarPorId_alumnoNoExiste_retornaVacio` | ID inventado | `assertTrue(resultado.isEmpty())` |

**crear (3 tests)**

| Test | Escenario | Asercion clave |
|------|----------|---------------|
| `crear_sinFechaRegistro_asignaFechaActual` | Sin fecha | `assertEquals(LocalDate.now(), resultado.getFechaRegistro())` |
| `crear_conFechaRegistro_conservaFechaOriginal` | Con fecha | `assertEquals(fechaPersonalizada, resultado.getFechaRegistro())` |
| `crear_alumnoNuevo_generaId` | ID null al inicio | `assertNotNull(resultado.getId())` |

El test de `crear_sinFechaRegistro_asignaFechaActual` es interesante porque verifica una **regla de negocio**: el servicio auto-asigna la fecha si no se proporciona. Esta logica esta en `AlumnoService.crear()`:

```java
public Alumno crear(Alumno alumno) {
    if (alumno.getFechaRegistro() == null) {
        alumno.setFechaRegistro(LocalDate.now());
    }
    return repository.save(alumno);
}
```

**actualizar (2 tests)**

| Test | Escenario | Asercion clave |
|------|----------|---------------|
| `actualizar_alumnoExiste_retornaAlumnoActualizado` | ID valido | `assertAll` verificando nombre, apellido, email actualizados |
| `actualizar_alumnoNoExiste_retornaVacio` | ID inexistente | `assertTrue(resultado.isEmpty())` |

**eliminar (3 tests)**

| Test | Escenario | Asercion clave |
|------|----------|---------------|
| `eliminar_alumnoExiste_retornaTrueYElimina` | ID valido | `assertTrue(resultado)` + verificar que ya no existe |
| `eliminar_alumnoNoExiste_retornaFalse` | ID inexistente | `assertFalse(resultado)` |
| `eliminar_unAlumno_noAfectaOtros` | 2 alumnos, eliminar 1 | `assertEquals(1, restantes.size())` |

El tercer test de eliminar es especialmente bueno: verifica que eliminar un alumno no elimina a los demas. Este tipo de test se llama "efecto colateral negativo" — verificas que algo que NO deberia pasar, efectivamente no paso.

---

## Como ejecutar los tests

Desde la terminal, en la carpeta del proyecto (`restSpringMongoJUnit/`):

```bash
mvn test
```

**No necesitas que MongoDB este corriendo.** Los tests usan el `FakeAlumnoRepository` — no tocan la base de datos.

### Salida esperada

```
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.academia.rest.entity.AlumnoTest
[INFO] Tests run: 8, Failures: 0, Errors: 0, Skipped: 0
[INFO] Running com.academia.rest.service.AlumnoServiceTest
[INFO] Tests run: 12, Failures: 0, Errors: 0, Skipped: 0
[INFO] -------------------------------------------------------
[INFO] Results:
[INFO]
[INFO] Tests run: 20, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO] BUILD SUCCESS
```

Si un test falla, Maven muestra:
- Que test fallo (nombre de la clase y el metodo)
- Que se esperaba vs que se obtuvo
- El mensaje de error que pusiste en la asercion

### Desde Eclipse

Clic derecho en el proyecto > **Run As** > **JUnit Test**. Eclipse muestra una barra verde si todos pasan, roja si alguno falla.

---

## Convencion de nombres

Todos los tests del proyecto siguen el patron:

```
metodo_escenario_resultadoEsperado
```

| Parte | Que describe | Ejemplo |
|-------|-------------|---------|
| `metodo` | Que metodo estamos probando | `listarTodos` |
| `escenario` | Bajo que condiciones | `sinAlumnos` |
| `resultadoEsperado` | Que deberia pasar | `retornaListaVacia` |

Ejemplos reales del proyecto:

| Nombre del metodo | metodo | escenario | resultado |
|-------------------|--------|----------|-----------|
| `constructorVacio_sinParametros_camposNulos` | constructorVacio | sinParametros | camposNulos |
| `buscarPorId_alumnoExiste_retornaAlumno` | buscarPorId | alumnoExiste | retornaAlumno |
| `crear_sinFechaRegistro_asignaFechaActual` | crear | sinFechaRegistro | asignaFechaActual |
| `eliminar_unAlumno_noAfectaOtros` | eliminar | unAlumno | noAfectaOtros |

Esta convencion tiene dos ventajas:
1. Al leer el nombre del test ya sabes que hace, sin necesidad de leer el codigo
2. Cuando un test falla, el nombre te dice inmediatamente que escenario esta roto

---

## Problemas comunes

### "No tests found"

El metodo de test no tiene la anotacion `@Test`:
```java
// MAL - falta @Test
void miTest() { ... }

// BIEN
@Test
void miTest() { ... }
```

O estas importando `@Test` de JUnit 4 en lugar de JUnit 5:
```java
// MAL - JUnit 4
import org.junit.Test;

// BIEN - JUnit 5
import org.junit.jupiter.api.Test;
```

### "expected: <X> but was: <Y>"

El valor esperado y el actual no coinciden. Revisa:
- Que el primer argumento de `assertEquals` sea el **esperado** y el segundo el **actual**
- Que no haya espacios o caracteres extra en los strings
- Que los tipos coincidan (un `int` no es igual a un `long`)

### El test pasa solo pero falla con los demas

Los tests se estan afectando entre si. Asegurate de usar `@BeforeEach` para crear estado fresco:
```java
@BeforeEach
void setUp() {
    // Nuevo repositorio vacio y nuevo servicio para cada test
    fakeRepository = new FakeAlumnoRepository();
    service = new AlumnoService(fakeRepository);
}
```

### "Cannot resolve symbol 'assertEquals'"

Falta el import estatico:
```java
import static org.junit.jupiter.api.Assertions.*;
```

### Los tests pasan pero el codigo de produccion falla

Los tests cubren la logica del servicio, no la conexion a MongoDB. Si el servicio funciona en los tests pero falla en produccion, el problema probablemente esta en la configuracion de MongoDB (URI, contenedor, etc.), no en la logica.

### assertAll muestra multiples errores

Eso es exactamente lo que debe hacer. `assertAll` ejecuta todas las verificaciones y reporta **todas** las que fallaron. Corrige cada error reportado.

---

## Resumen

| Concepto | Que aprendimos |
|----------|---------------|
| `@Test` | Marca un metodo como test |
| `@DisplayName` | Nombre legible para el reporte |
| `@BeforeEach` | Estado fresco antes de cada test |
| Patron AAA | Arrange, Act, Assert |
| `assertEquals` | Verifica igualdad |
| `assertNull` / `assertNotNull` | Verifica presencia o ausencia de valor |
| `assertTrue` / `assertFalse` | Verifica condiciones booleanas |
| `assertAll` | Verifica multiples cosas a la vez |
| Fake/Stub | Implementacion falsa para tests sin dependencias externas |
| Convencion de nombres | `metodo_escenario_resultadoEsperado` |

**Siguiente paso:** En el proyecto `springBatchV2MongoMockito` veremos como Mockito resuelve el problema de los fakes manuales — en lugar de escribir 23 metodos a mano, Mockito crea la implementacion falsa automaticamente en una sola linea.
