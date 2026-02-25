package com.academia.rest.service;

import com.academia.rest.entity.Alumno;
import com.academia.rest.fake.FakeAlumnoRepository;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests del servicio AlumnoService usando un FakeAlumnoRepository.
 *
 * Conceptos clave:
 * - @BeforeEach: se ejecuta antes de CADA test (estado fresco)
 * - Patron AAA: Arrange (preparar), Act (ejecutar), Assert (verificar)
 * - No se necesita base de datos ni Spring para ejecutar estos tests
 */
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

    // =====================================================================
    //  listarTodos()
    // =====================================================================

    @Test
    @DisplayName("listarTodos: lista vacia cuando no hay alumnos")
    void listarTodos_sinAlumnos_retornaListaVacia() {
        // Arrange - el repositorio ya esta vacio por el setUp

        // Act
        List<Alumno> resultado = service.listarTodos();

        // Assert
        assertTrue(resultado.isEmpty(), "La lista debe estar vacia");
    }

    @Test
    @DisplayName("listarTodos: retorna todos los alumnos existentes")
    void listarTodos_conAlumnos_retornaTodos() {
        // Arrange - insertamos 2 alumnos via el servicio
        Alumno alumno1 = crearAlumno("Juan", "Perez", "juan@correo.com");
        Alumno alumno2 = crearAlumno("Maria", "Lopez", "maria@correo.com");
        service.crear(alumno1);
        service.crear(alumno2);

        // Act
        List<Alumno> resultado = service.listarTodos();

        // Assert
        assertEquals(2, resultado.size(), "Debe haber 2 alumnos");
    }

    // =====================================================================
    //  buscarPorId()
    // =====================================================================

    @Test
    @DisplayName("buscarPorId: encuentra un alumno existente")
    void buscarPorId_alumnoExiste_retornaAlumno() {
        // Arrange
        Alumno alumno = crearAlumno("Juan", "Perez", "juan@correo.com");
        Alumno creado = service.crear(alumno);

        // Act
        Optional<Alumno> resultado = service.buscarPorId(creado.getId());

        // Assert
        assertTrue(resultado.isPresent(), "Debe encontrar al alumno");
        assertEquals("Juan", resultado.get().getNombre());
    }

    @Test
    @DisplayName("buscarPorId: retorna vacio para ID inexistente")
    void buscarPorId_alumnoNoExiste_retornaVacio() {
        // Arrange - no insertamos nada

        // Act
        Optional<Alumno> resultado = service.buscarPorId("id-que-no-existe");

        // Assert
        assertTrue(resultado.isEmpty(), "No debe encontrar al alumno");
    }

    // =====================================================================
    //  crear()
    // =====================================================================

    @Test
    @DisplayName("crear: asigna fecha de registro automaticamente si no se proporciona")
    void crear_sinFechaRegistro_asignaFechaActual() {
        // Arrange
        Alumno alumno = crearAlumno("Juan", "Perez", "juan@correo.com");
        // No asignamos fechaRegistro (queda null)

        // Act
        Alumno resultado = service.crear(alumno);

        // Assert
        assertNotNull(resultado.getFechaRegistro(), "Debe asignar fecha automaticamente");
        assertEquals(LocalDate.now(), resultado.getFechaRegistro());
    }

    @Test
    @DisplayName("crear: respeta la fecha de registro si ya viene proporcionada")
    void crear_conFechaRegistro_conservaFechaOriginal() {
        // Arrange
        Alumno alumno = crearAlumno("Juan", "Perez", "juan@correo.com");
        LocalDate fechaPersonalizada = LocalDate.of(2025, 6, 15);
        alumno.setFechaRegistro(fechaPersonalizada);

        // Act
        Alumno resultado = service.crear(alumno);

        // Assert
        assertEquals(fechaPersonalizada, resultado.getFechaRegistro(),
                "Debe conservar la fecha proporcionada");
    }

    @Test
    @DisplayName("crear: genera un ID automaticamente")
    void crear_alumnoNuevo_generaId() {
        // Arrange
        Alumno alumno = crearAlumno("Juan", "Perez", "juan@correo.com");
        assertNull(alumno.getId(), "Precondicion: el ID debe ser null antes de crear");

        // Act
        Alumno resultado = service.crear(alumno);

        // Assert
        assertNotNull(resultado.getId(), "El servicio debe generar un ID");
        assertFalse(resultado.getId().isEmpty(), "El ID no debe estar vacio");
    }

    // =====================================================================
    //  actualizar()
    // =====================================================================

    @Test
    @DisplayName("actualizar: modifica los datos de un alumno existente")
    void actualizar_alumnoExiste_retornaAlumnoActualizado() {
        // Arrange - creamos un alumno original
        Alumno original = crearAlumno("Juan", "Perez", "juan@correo.com");
        Alumno creado = service.crear(original);
        String idCreado = creado.getId();

        // Preparamos los datos actualizados
        Alumno datosNuevos = crearAlumno("Juan Carlos", "Perez Garcia", "jc@correo.com");

        // Act
        Optional<Alumno> resultado = service.actualizar(idCreado, datosNuevos);

        // Assert
        assertTrue(resultado.isPresent(), "Debe retornar el alumno actualizado");
        assertAll("Datos actualizados",
            () -> assertEquals("Juan Carlos", resultado.get().getNombre()),
            () -> assertEquals("Perez Garcia", resultado.get().getApellido()),
            () -> assertEquals("jc@correo.com", resultado.get().getEmail())
        );
    }

    @Test
    @DisplayName("actualizar: retorna vacio si el alumno no existe")
    void actualizar_alumnoNoExiste_retornaVacio() {
        // Arrange
        Alumno datosNuevos = crearAlumno("Juan", "Perez", "juan@correo.com");

        // Act
        Optional<Alumno> resultado = service.actualizar("id-inexistente", datosNuevos);

        // Assert
        assertTrue(resultado.isEmpty(), "No debe encontrar al alumno para actualizar");
    }

    // =====================================================================
    //  eliminar()
    // =====================================================================

    @Test
    @DisplayName("eliminar: retorna true y elimina al alumno existente")
    void eliminar_alumnoExiste_retornaTrueYElimina() {
        // Arrange
        Alumno alumno = crearAlumno("Juan", "Perez", "juan@correo.com");
        Alumno creado = service.crear(alumno);

        // Act
        boolean resultado = service.eliminar(creado.getId());

        // Assert
        assertTrue(resultado, "Debe retornar true al eliminar");
        // Verificamos que ya no existe
        assertTrue(service.buscarPorId(creado.getId()).isEmpty(),
                "El alumno ya no debe existir despues de eliminar");
    }

    @Test
    @DisplayName("eliminar: retorna false si el alumno no existe")
    void eliminar_alumnoNoExiste_retornaFalse() {
        // Arrange - no insertamos nada

        // Act
        boolean resultado = service.eliminar("id-que-no-existe");

        // Assert
        assertFalse(resultado, "Debe retornar false si no existe");
    }

    @Test
    @DisplayName("eliminar: no afecta a otros alumnos")
    void eliminar_unAlumno_noAfectaOtros() {
        // Arrange
        Alumno alumno1 = crearAlumno("Juan", "Perez", "juan@correo.com");
        Alumno alumno2 = crearAlumno("Maria", "Lopez", "maria@correo.com");
        Alumno creado1 = service.crear(alumno1);
        service.crear(alumno2);

        // Act - eliminamos solo al primero
        service.eliminar(creado1.getId());

        // Assert - el segundo debe seguir existiendo
        List<Alumno> restantes = service.listarTodos();
        assertEquals(1, restantes.size(), "Debe quedar 1 alumno");
        assertEquals("Maria", restantes.get(0).getNombre());
    }

    // =====================================================================
    //  Metodo auxiliar para crear alumnos de prueba
    // =====================================================================

    private Alumno crearAlumno(String nombre, String apellido, String email) {
        Alumno alumno = new Alumno();
        alumno.setNombre(nombre);
        alumno.setApellido(apellido);
        alumno.setEmail(email);
        return alumno;
    }
}
