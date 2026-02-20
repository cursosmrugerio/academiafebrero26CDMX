package como.curso.v1;

public class Principal {

	public static void main(String[] args) {
		
		Fabrica fab2 = new FabricaMty();
		fab2.producir();
		
		Fabrica fab3 = new FabricaOax();
		fab3.producir();
	}

}
