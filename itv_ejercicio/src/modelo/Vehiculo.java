package modelo;
import excepciones.CamposVacioException;
import excepciones.DniException;
import excepciones.MatriculaException;

public class Vehiculo {

    private String matricula;
    private String nombre;
    private String apellidos;
    private String dni;
    private String identificador;

    public Vehiculo(String matricula, String nombre, String apellidos, String dni) throws MatriculaException, DniException, CamposVacioException {
        setNombre(nombre);
        setApellidos(apellidos);
        setDni(dni);
        setMatricula(matricula);
        generaIdentificador();
    }

    private void generaIdentificador() {
        this.identificador = (nombre.substring(0,1) + apellidos.substring(0,1) + dni.substring(4,7));
    }

    // Getters and Setters
    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) throws MatriculaException{
        
        if (!matricula.matches("\\d{4}[A-Z]{3}")) {
            throw new MatriculaException();
        }

        this.matricula = matricula;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) throws CamposVacioException{
        if (nombre.length() <= 0) {
            throw new CamposVacioException();
        }
        this.nombre = nombre;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) throws CamposVacioException{
        if (apellidos.length() <= 0) {
            throw new CamposVacioException();
        }
        this.apellidos = apellidos;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) throws DniException{
        
        String letrasDni = "TRWAGMYFPDXBNJZSQVHLCKE";

        if (dni.length() != 9)
            throw new DniException();
        String numDniC = dni.substring(0, 8);
        char letraDni = dni.charAt(8);
        int num = 0;

        try { // Para ver si los 8 primeros son números
            num = Integer.parseInt(numDniC);
        } catch (NumberFormatException e) {
            throw new DniException();
        }

        int resto = num % 23;

        if (letrasDni.charAt(resto) != letraDni) {
            throw new DniException();
        }
        this.dni = dni;
    }

    public String getIdentificador() {
        return identificador;
    }

    public void setIdentificador(String identificador) {
        this.identificador = identificador;
    }

    @Override
    public String toString() {
        return "Vehiculo [matricula=" + matricula + ", nombre=" + nombre + ", apellidos=" + apellidos + ", dni=" + dni
                + ", identificador=" + identificador + "]";
    }

    
}