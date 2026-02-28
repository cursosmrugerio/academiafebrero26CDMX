package com.academia.mockito;

/**
 * DTO (Data Transfer Object) que representa los datos de una solicitud de credito.
 *
 * Este objeto viaja entre capas: el cliente lo crea con sus datos
 * y el procesador lo envia al servicio de riesgo para evaluacion.
 *
 * En el contexto de Mockito, este objeto es "real" (no se mockea),
 * porque es un simple contenedor de datos sin logica compleja.
 */
public class SolicitudCredito {

    private String nombreCliente;   // Nombre completo del solicitante
    private double montoSolicitado; // Cantidad de dinero que solicita
    private double ingresoMensual;  // Ingreso mensual declarado del cliente

    public SolicitudCredito(String nombreCliente, double montoSolicitado, double ingresoMensual) {
        this.nombreCliente = nombreCliente;
        this.montoSolicitado = montoSolicitado;
        this.ingresoMensual = ingresoMensual;
    }

    public String getNombreCliente() {
        return nombreCliente;
    }

    public double getMontoSolicitado() {
        return montoSolicitado;
    }

    public double getIngresoMensual() {
        return ingresoMensual;
    }
}
