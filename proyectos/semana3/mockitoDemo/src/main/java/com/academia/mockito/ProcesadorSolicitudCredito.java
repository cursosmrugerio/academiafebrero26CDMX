package com.academia.mockito;

/**
 * Clase de negocio que procesa solicitudes de credito.
 *
 * Depende de ServicioCalculoRiesgo (interface) inyectada por constructor.
 * Esta clase NO sabe ni le importa como se calcula el riesgo,
 * solo consume el resultado para tomar decisiones.
 */
public class ProcesadorSolicitudCredito {

    private final ServicioCalculoRiesgo servicioRiesgo;

    // Inyeccion por constructor: recibe la interface, no una implementacion concreta
    public ProcesadorSolicitudCredito(ServicioCalculoRiesgo servicioRiesgo) {
        this.servicioRiesgo = servicioRiesgo;
    }

    public ResultadoSolicitud procesar(SolicitudCredito solicitud) {

        // Paso 1: verificar si tiene deudas vigentes
        if (servicioRiesgo.tieneDeudasVigentes(solicitud.getNombreCliente())) {
            return new ResultadoSolicitud(false,
                    "Rechazado: el cliente tiene deudas vigentes");
        }

        // Paso 2: obtener puntaje de riesgo (operacion compleja simulada)
        int puntaje = servicioRiesgo.calcularPuntajeRiesgo(solicitud);

        // Paso 3: tomar decision basada en el puntaje
        if (puntaje >= 70) {
            return new ResultadoSolicitud(true,
                    "Aprobado: puntaje de riesgo " + puntaje);
        } else if (puntaje >= 40) {
            return new ResultadoSolicitud(false,
                    "Rechazado: puntaje insuficiente (" + puntaje + "). Requiere minimo 70");
        } else {
            return new ResultadoSolicitud(false,
                    "Rechazado: riesgo muy alto. Puntaje: " + puntaje);
        }
    }
}
