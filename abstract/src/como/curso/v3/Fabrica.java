package como.curso.v3;

public abstract class Fabrica {
	
	void producir() {
		System.out.println("PRODUCIR!!!!");
	}
	
	final void entregarProducto() {
		System.out.println("Inicio Producción");
		producir();
		System.out.println("Fin Producción");
	}

}
