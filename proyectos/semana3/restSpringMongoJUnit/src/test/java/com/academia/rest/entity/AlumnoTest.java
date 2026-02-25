package com.academia.rest.entity;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Tests de la entidad Alumno.
 *
 * Primer contacto con JUnit 5: aprendemos a usar las aserciones basicas
 * (assertEquals, assertNotNull, assertNull, assertAll) y la anotacion @Test.
 */
class AlumnoTest {

    // =====================================================================
    //  Tests del constructor y estado inicial
    // =====================================================================

    @Test
    @DisplayName("Constructor vacio crea alumno con campos nulos")
    void constructorVacio_sinParametros_camposNulos() {
        // Arrange & Act
        Alumno alumno = new Alumno();

        // Assert - assertAll agrupa varias verificaciones: si una falla,
        //          las demas siguen ejecutandose (a diferencia de asserts sueltos)
        assertAll("Estado inicial del alumno",
            () -> assertNull(alumno.getId(), "id debe ser null"),
            () -> assertNull(alumno.getNombre(), "nombre debe ser null"),
            () -> assertNull(alumno.getApellido(), "apellido debe ser null"),
            () -> assertNull(alumno.getEmail(), "email debe ser null"),
            () -> assertNull(alumno.getFechaRegistro(), "fechaRegistro debe ser null")
        );
    }

    // =====================================================================
    //  Tests de getters y setters
    // =====================================================================

    @Test
    @DisplayName("setNombre y getNombre guardan y devuelven el nombre")
    void setNombre_valorValido_retornaMismoValor() {
        // Arrange
        Alumno alumno = new Alumno();

        // Act
        alumno.setNombre("Juan");

        // Assert
        assertEquals("Juan", alumno.getNombre());
    }

    @Test
    @DisplayName("setApellido y getApellido guardan y devuelven el apellido")
    void setApellido_valorValido_retornaMismoValor() {
        // Arrange
        Alumno alumno = new Alumno();

        // Act
        alumno.setApellido("Perez");

        // Assert
        assertEquals("Perez", alumno.getApellido());
    }

    @Test
    @DisplayName("setEmail y getEmail guardan y devuelven el email")
    void setEmail_valorValido_retornaMismoValor() {
        // Arrange
        Alumno alumno = new Alumno();

        // Act
        alumno.setEmail("juan@correo.com");

        // Assert
        assertEquals("juan@correo.com", alumno.getEmail());
    }

    @Test
    @DisplayName("setId y getId guardan y devuelven el ID")
    void setId_valorValido_retornaMismoValor() {
        // Arrange
        Alumno alumno = new Alumno();

        // Act
        alumno.setId("abc123");

        // Assert
        assertEquals("abc123", alumno.getId());
    }

    // =====================================================================
    //  Tests con LocalDate
    // =====================================================================

    @Test
    @DisplayName("setFechaRegistro guarda la fecha correctamente")
    void setFechaRegistro_fechaValida_retornaMismaFecha() {
        // Arrange
        Alumno alumno = new Alumno();
        LocalDate fecha = LocalDate.of(2026, 2, 24);

        // Act
        alumno.setFechaRegistro(fecha);

        // Assert
        assertEquals(fecha, alumno.getFechaRegistro());
    }

    @Test
    @DisplayName("La fecha de registro puede ser la fecha actual")
    void setFechaRegistro_fechaActual_retornaHoy() {
        // Arrange
        Alumno alumno = new Alumno();
        LocalDate hoy = LocalDate.now();

        // Act
        alumno.setFechaRegistro(hoy);

        // Assert
        assertNotNull(alumno.getFechaRegistro(), "La fecha no debe ser null");
        assertEquals(hoy, alumno.getFechaRegistro());
    }

    // =====================================================================
    //  Test con assertAll: verificar multiples propiedades a la vez
    // =====================================================================

    @Test
    @DisplayName("assertAll verifica todas las propiedades del alumno")
    void alumnoCompleto_todasLasPropiedades_verificaConAssertAll() {
        // Arrange
        Alumno alumno = new Alumno();
        LocalDate fecha = LocalDate.of(2026, 1, 15);

        // Act
        alumno.setId("xyz789");
        alumno.setNombre("Maria");
        alumno.setApellido("Lopez");
        alumno.setEmail("maria@correo.com");
        alumno.setFechaRegistro(fecha);

        // Assert - assertAll ejecuta TODAS las aserciones aunque alguna falle
        assertAll("Propiedades del alumno",
            () -> assertEquals("xyz789", alumno.getId()),
            () -> assertEquals("Maria", alumno.getNombre()),
            () -> assertEquals("Lopez", alumno.getApellido()),
            () -> assertEquals("maria@correo.com", alumno.getEmail()),
            () -> assertEquals(LocalDate.of(2026, 1, 15), alumno.getFechaRegistro())
        );
    }
}
