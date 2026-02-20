package como.curso.v0;

public class Principal {

	public static void main(String[] args) {

		Fabrica fab1 = new Fabrica();
		fab1.producir();
		
		Fabrica fab2 = new FabricaMty();
		fab2.producir();
		
		Fabrica fab3 = new FabricaOax();
		fab3.producir();
	}

}
