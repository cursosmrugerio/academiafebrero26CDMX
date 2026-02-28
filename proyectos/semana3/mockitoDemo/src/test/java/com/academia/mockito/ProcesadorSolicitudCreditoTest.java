package com.academia.mockito;

// --- Imports de JUnit 5 ---
import org.junit.jupiter.api.DisplayName;                  // Nombre descriptivo para cada test
import org.junit.jupiter.api.Test;                          // Marca un metodo como test
import org.junit.jupiter.api.extension.ExtendWith;          // Registra extensiones (como Mockito)

// --- Imports de Mockito ---
import org.mockito.InjectMocks;                             // Inyecta los mocks en la clase bajo prueba
import org.mockito.Mock;                                    // Crea un objeto mock (falso)
import org.mockito.junit.jupiter.MockitoExtension;          // Extension que activa @Mock y @InjectMocks

// --- Imports estaticos de JUnit 5 (assertions) ---
import static org.junit.jupiter.api.Assertions.*;           // assertTrue, assertFalse, assertEquals

// --- Imports estaticos de Mockito (metodos principales) ---
// when()          -> define que devuelve un mock cuando se llama a un metodo
// verify()        -> verifica que un metodo del mock fue invocado
// never()         -> verifica que un metodo NUNCA fue llamado
// times(n)        -> verifica que un metodo fue llamado exactamente n veces
// any()           -> matcher que acepta cualquier argumento
// verifyNoMoreInteractions() -> confirma que no hubo mas llamadas al mock
import static org.mockito.Mockito.*;

/**
 * Pruebas unitarias del ProcesadorSolicitudCredito.
 *
 * Punto clave: ServicioCalculoRiesgo NO tiene implementacion real.
 * Mockito crea un objeto "falso" que responde lo que nosotros le indiquemos.
 * Asi podemos probar TODA la logica del procesador sin depender del servicio real.
 */
@ExtendWith(MockitoExtension.class)  // Activa las anotaciones de Mockito
class ProcesadorSolicitudCreditoTest {

    @Mock  // Mockito crea un objeto falso que implementa la interface
    private ServicioCalculoRiesgo servicioRiesgo;

    @InjectMocks  // Mockito inyecta el mock en el constructor del procesador
    private ProcesadorSolicitudCredito procesador;

    // -----------------------------------------------------------------------
    // Escenario 1: Cliente con buen puntaje y sin deudas -> APROBADO
    // -----------------------------------------------------------------------
    @Test
    @DisplayName("Cliente sin deudas y puntaje alto -> credito aprobado")
    void clienteSinDeudasYPuntajeAlto_debeAprobar() {
        // ARRANGE (preparar): definir que devuelve el mock
        SolicitudCredito solicitud = new SolicitudCredito("Carlos Lopez", 50000, 30000);

        // when().thenReturn() -> le decimos al mock que responder cuando lo llamen
        when(servicioRiesgo.tieneDeudasVigentes("Carlos Lopez")).thenReturn(false);
        when(servicioRiesgo.calcularPuntajeRiesgo(solicitud)).thenReturn(85);

        // ACT (actuar): ejecutar la logica real del procesador
        ResultadoSolicitud resultado = procesador.procesar(solicitud);

        // ASSERT (verificar): comprobar que el resultado es correcto
        assertTrue(resultado.isAprobado());
        assertEquals("Aprobado: puntaje de riesgo 85", resultado.getMensaje());

        // verify() -> confirmar que el mock fue invocado correctamente
        verify(servicioRiesgo).tieneDeudasVigentes("Carlos Lopez");
        verify(servicioRiesgo).calcularPuntajeRiesgo(solicitud);
    }

    // -----------------------------------------------------------------------
    // Escenario 2: Cliente con deudas vigentes -> RECHAZADO (ni siquiera calcula riesgo)
    // -----------------------------------------------------------------------
    @Test
    @DisplayName("Cliente con deudas vigentes -> rechazado sin calcular riesgo")
    void clienteConDeudas_debeRechazarSinCalcularRiesgo() {
        // ARRANGE
        SolicitudCredito solicitud = new SolicitudCredito("Ana Martinez", 100000, 45000);

        when(servicioRiesgo.tieneDeudasVigentes("Ana Martinez")).thenReturn(true);

        // ACT
        ResultadoSolicitud resultado = procesador.procesar(solicitud);

        // ASSERT
        assertFalse(resultado.isAprobado());
        assertEquals("Rechazado: el cliente tiene deudas vigentes", resultado.getMensaje());

        // verify + never() -> confirmar que calcularPuntajeRiesgo NUNCA fue llamado
        verify(servicioRiesgo).tieneDeudasVigentes("Ana Martinez");
        verify(servicioRiesgo, never()).calcularPuntajeRiesgo(any());
    }

    // -----------------------------------------------------------------------
    // Escenario 3: Cliente sin deudas pero puntaje medio -> RECHAZADO
    // -----------------------------------------------------------------------
    @Test
    @DisplayName("Cliente sin deudas pero puntaje insuficiente -> rechazado")
    void clienteSinDeudasPuntajeMedio_debeRechazar() {
        // ARRANGE
        SolicitudCredito solicitud = new SolicitudCredito("Pedro Gomez", 80000, 20000);

        when(servicioRiesgo.tieneDeudasVigentes("Pedro Gomez")).thenReturn(false);
        when(servicioRiesgo.calcularPuntajeRiesgo(solicitud)).thenReturn(55);

        // ACT
        ResultadoSolicitud resultado = procesador.procesar(solicitud);

        // ASSERT
        assertFalse(resultado.isAprobado());
        assertTrue(resultado.getMensaje().contains("puntaje insuficiente"));
    }

    // -----------------------------------------------------------------------
    // Escenario 4: Cliente sin deudas pero riesgo muy alto -> RECHAZADO
    // -----------------------------------------------------------------------
    @Test
    @DisplayName("Cliente con riesgo muy alto -> rechazado con mensaje critico")
    void clienteConRiesgoMuyAlto_debeRechazarConMensajeCritico() {
        // ARRANGE
        SolicitudCredito solicitud = new SolicitudCredito("Luis Ramirez", 200000, 15000);

        when(servicioRiesgo.tieneDeudasVigentes("Luis Ramirez")).thenReturn(false);
        when(servicioRiesgo.calcularPuntajeRiesgo(solicitud)).thenReturn(20);

        // ACT
        ResultadoSolicitud resultado = procesador.procesar(solicitud);

        // ASSERT
        assertFalse(resultado.isAprobado());
        assertTrue(resultado.getMensaje().contains("riesgo muy alto"));
    }

    // -----------------------------------------------------------------------
    // Escenario 5: Verificar cuantas veces se llamo al servicio
    // -----------------------------------------------------------------------
    @Test
    @DisplayName("Verificar que el servicio de riesgo se llama exactamente 1 vez")
    void verificarNumeroDeInvocaciones() {
        // ARRANGE
        SolicitudCredito solicitud = new SolicitudCredito("Maria Torres", 30000, 25000);

        when(servicioRiesgo.tieneDeudasVigentes("Maria Torres")).thenReturn(false);
        when(servicioRiesgo.calcularPuntajeRiesgo(solicitud)).thenReturn(90);

        // ACT
        procesador.procesar(solicitud);

        // ASSERT: verificar numero exacto de invocaciones
        verify(servicioRiesgo, times(1)).tieneDeudasVigentes("Maria Torres");
        verify(servicioRiesgo, times(1)).calcularPuntajeRiesgo(solicitud);

        // verifyNoMoreInteractions -> confirmar que no hubo llamadas adicionales
        verifyNoMoreInteractions(servicioRiesgo);
    }
}
