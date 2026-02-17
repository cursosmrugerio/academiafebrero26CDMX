package com.curso.v00;

public final class DiaSemana {

    private final String nombre;
    private final int ordinal;

    public static final DiaSemana LUNES     = new DiaSemana("LUNES", 0);
    public static final DiaSemana MARTES    = new DiaSemana("MARTES", 1);
    public static final DiaSemana MIERCOLES = new DiaSemana("MIERCOLES", 2);
    public static final DiaSemana JUEVES    = new DiaSemana("JUEVES", 3);
    public static final DiaSemana VIERNES   = new DiaSemana("VIERNES", 4);
    public static final DiaSemana SABADO    = new DiaSemana("SABADO", 5);
    public static final DiaSemana DOMINGO   = new DiaSemana("DOMINGO", 6);

    private static final DiaSemana[] VALUES = {
        LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO
    };

    // Constructor privado para evitar instancias externas
    private DiaSemana(String nombre, int ordinal) {
        this.nombre = nombre;
        this.ordinal = ordinal;
    }

    public String name() {
        return nombre;
    }

    public int ordinal() {
        return ordinal;
    }

    public static DiaSemana[] values() {
        return VALUES.clone();
    }

    public static DiaSemana valueOf(String nombre) {
        for (DiaSemana dia : VALUES) {
            if (dia.nombre.equals(nombre)) {
                return dia;
            }
        }
        throw new IllegalArgumentException("No existe la constante: " + nombre);
    }

    @Override
    public String toString() {
        return nombre;
    }
}
