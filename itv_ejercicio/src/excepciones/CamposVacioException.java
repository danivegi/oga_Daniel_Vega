package excepciones;

public class CamposVacioException extends Exception{

    public CamposVacioException() {
        super("El mensaje está vacío");
    }

}
