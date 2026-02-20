package como.curso.v2;

public class Principal {

	public static void main(String[] args) {
		
		Fabrica fab1 = new FabricaMty();
		fab1.entregarProducto();
		
		Fabrica fab2 = new FabricaOax();
		fab2.entregarProducto();
	}

}
