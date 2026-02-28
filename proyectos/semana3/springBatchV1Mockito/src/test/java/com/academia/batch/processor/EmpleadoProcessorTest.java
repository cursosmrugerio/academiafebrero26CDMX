package com.academia.batch.processor;

import com.academia.batch.model.Empleado;
import com.academia.batch.service.BonoService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

/**
 * Clase de prueba para aprender Mockito.
 * 
 * @ExtendWith(MockitoExtension.class) inicializa los mocks automáticamente.
 */
@ExtendWith(MockitoExtension.class)
public class EmpleadoProcessorTest {

    /**
     * @Mock crea un "doble" o simulacro de la clase.
     * No ejecuta el código real de BonoService.
     */
    @Mock
    private BonoService bonoService;

    /**
     * @InjectMocks crea una instancia real de EmpleadoProcessor
     * e inyecta automáticamente el mock de 'bonoService' en su constructor.
     */
    @InjectMocks
    private EmpleadoProcessor empleadoProcessor;

    private Empleado empleado;

    @BeforeEach
    void setUp() {
        empleado = new Empleado();
        empleado.setNombre("juan perez");
        empleado.setSalario(1000.0);
    }

    @Test
    void testProcess_DebeConvertirMayusculasYCalcularBonoConMock() {
        // 1. STUBBING (Definir comportamiento del Mock)
        // "Cuando el mock llame a calcularBono con cualquier double, entonces retorna 150.0"
        // Esto aísla la prueba: no importa si la lógica real de BonoService cambia,
        // aquí controlamos el resultado para probar SOLO el procesador.
        when(bonoService.calcularBono(anyDouble())).thenReturn(150.0);

        // 2. EJECUCIÓN
        Empleado resultado = empleadoProcessor.process(empleado);

        // 3. ASSERTIONS (Verificaciones de estado)
        assertEquals("JUAN PEREZ", resultado.getNombre(), "El nombre debería estar en mayúsculas");
        assertEquals(150.0, resultado.getBono(), "El bono debería ser el valor retornado por el mock");

        // 4. VERIFICATION (Verificaciones de comportamiento)
        // Verificamos que el procesador REALMENTE llamó al servicio una vez.
        verify(bonoService, times(1)).calcularBono(1000.0);
    }
}
