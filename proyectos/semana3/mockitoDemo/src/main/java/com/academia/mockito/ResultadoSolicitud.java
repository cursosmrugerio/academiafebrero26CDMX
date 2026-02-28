package com.academia.mockito;

/**
 * DTO que representa el resultado de evaluar una solicitud de credito.
 *
 * Contiene la decision (aprobado o rechazado) y un mensaje descriptivo.
 * Este objeto es lo que retorna el procesador despues de consultar
 * al servicio de riesgo y aplicar las reglas de negocio.
 *
 * Al igual que SolicitudCredito, este DTO es "real" en los tests,
 * no se mockea porque solo transporta datos.
 */
public class ResultadoSolicitud {

    private boolean aprobado; // true = credito aprobado, false = rechazado
    private String mensaje;   // Razon de la decision (para mostrar al cliente)

    public ResultadoSolicitud(boolean aprobado, String mensaje) {
        this.aprobado = aprobado;
        this.mensaje = mensaje;
    }

    public boolean isAprobado() {
        return aprobado;
    }

    public String getMensaje() {
        return mensaje;
    }
}
