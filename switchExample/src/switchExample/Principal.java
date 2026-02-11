package switchExample;

public class Principal {

	public static void main(String[] args) {

		String dia = "JUEVES";
		
		final String domingo = "DOMINGO";
		
		switch(dia) {
		
		default : System.out.println("Dia 6");
				  
		case domingo: System.out.println("Dia 0");
				break;
		case "LUNES": System.out.println("Dia 1");
				break;
		case "MARTES": System.out.println("Dia 2");
				break;
		case "MIERCOLES": System.out.println("Dia 3");
		case "VIERNES": System.out.println("Dia 4");
		
		}
		
		
		
	}

}
