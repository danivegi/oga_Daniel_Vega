package vista;

import excepciones.CamposVacioException;
import excepciones.DniException;
import excepciones.MatriculaException;
import modelo.Vehiculo;

public class Main {

    public static void main(String[] args) throws CamposVacioException {

        String nombre = "Luis";
        String apellidos = "Garcia Perez";
        String dni = "32098557X";
        String matricula = "1224ABC";
        String identificador = "";
        Vehiculo vehiculo = null;
        try {
            vehiculo = new Vehiculo(matricula, nombre, apellidos, dni);
            System.out.println(vehiculo);
        } catch (DniException | MatriculaException e) {
            // TODO Auto-generated catch block
            System.out.println(e.getMessage());
        }
    }

}
