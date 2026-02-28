package com.academia.mockito;

/**
 * Interface que representa una operacion compleja de calculo de riesgo crediticio.
 *
 * En un escenario real, la implementacion podria:
 * - Consultar buros de credito externos
 * - Ejecutar modelos de machine learning
 * - Acceder a bases de datos de historial financiero
 *
 * Para este demo, NO existe implementacion real.
 * Mockito simulara su comportamiento en las pruebas.
 */
public interface ServicioCalculoRiesgo {

    /**
     * Calcula el puntaje de riesgo de un cliente.
     * @param solicitud datos de la solicitud de credito
     * @return puntaje entre 0 (riesgo maximo) y 100 (sin riesgo)
     */
    int calcularPuntajeRiesgo(SolicitudCredito solicitud);

    /**
     * Verifica si el cliente tiene deudas vigentes en el sistema financiero.
     * @param nombreCliente nombre del cliente a verificar
     * @return true si tiene deudas vigentes
     */
    boolean tieneDeudasVigentes(String nombreCliente);
}
