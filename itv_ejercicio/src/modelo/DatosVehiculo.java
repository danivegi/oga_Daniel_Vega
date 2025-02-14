package modelo;
import java.util.Calendar;

public class DatosVehiculo {

    private long entrada;
    private long salida;

    public DatosVehiculo() {
        this.entrada = Reloj.ahora();
    }

    public void atiende() {
        this.salida = Reloj.ahora();
        long tiempoEspera = salida - entrada;
        System.out.println("Tiempo de espera: " + tiempoEspera + " ms");
    }

    public long getTiempoEspera() {
        return (salida - entrada) / 1000;
    }

}
