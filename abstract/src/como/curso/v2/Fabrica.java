package como.curso.v2;

public abstract class Fabrica {
	
	abstract void producir();
	
	final void entregarProducto() {
		System.out.println("Inicio Producción");
		producir();
		System.out.println("Fin Producción");
	}

}
