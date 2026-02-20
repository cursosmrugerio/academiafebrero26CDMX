package como.curso.v3;

public class Principal {

	public static void main(String[] args) {
		
		Fabrica fab1 = new FabricaMty();
		fab1.entregarProducto();
		
		Fabrica fab2 = new FabricaOax();
		fab2.entregarProducto();
		
		System.out.println("Tlaxcala");
		Fabrica fab3 = new FabricaTlaxcala(); //No sobreescribio el metodo
		fab3.entregarProducto();
	}

}
