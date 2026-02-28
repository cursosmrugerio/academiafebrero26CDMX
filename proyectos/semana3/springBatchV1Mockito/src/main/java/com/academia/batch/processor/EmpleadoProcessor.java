package com.academia.batch.processor;

import com.academia.batch.model.Empleado;
import com.academia.batch.service.BonoService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.batch.item.ItemProcessor;

// Step 1 - Processor: transforma el empleado leido del CSV
public class EmpleadoProcessor implements ItemProcessor<Empleado, Empleado> {

    private static final Logger log = LoggerFactory.getLogger(EmpleadoProcessor.class);

    // Dependencia que queremos "aislar" durante las pruebas unitarias.
    private final BonoService bonoService;

    // El uso del constructor nos permite inyectar el Mock directamente
    public EmpleadoProcessor(BonoService bonoService) {
        this.bonoService = bonoService;
    }

    @Override
    public Empleado process(Empleado empleado) {
        // Lógica: transformar nombre a mayúsculas
        empleado.setNombre(empleado.getNombre().toUpperCase());

        // Usamos el servicio externo para calcular el bono.
        // En la prueba con Mockito, simularemos el comportamiento de calcularBono
        double bono = bonoService.calcularBono(empleado.getSalario());
        empleado.setBono(bono);

        log.info("Step 1 - Procesando: {}", empleado);
        return empleado;
    }
}
