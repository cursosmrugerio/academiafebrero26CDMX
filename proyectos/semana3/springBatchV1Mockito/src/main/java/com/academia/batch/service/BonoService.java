package com.academia.batch.service;

import org.springframework.stereotype.Service;

/**
 * Servicio encargado de la lógica de cálculo de bonos.
 * En una prueba unitaria con Mockito, simularemos este servicio
 * para probar el procesador de forma aislada.
 */
@Service
public class BonoService {

    public double calcularBono(double salario) {
        // Imagina que aquí hay una lógica compleja, llamadas a otros servicios o DB.
        // Mockito nos permite evitar que esta lógica se ejecute durante la prueba del procesador.
        return salario * 0.10;
    }
}
