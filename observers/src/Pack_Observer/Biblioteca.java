package Pack_Observer;

public class Biblioteca{
    public void devolver_Libro(Libro libro){
        if (libro.getEstado().equals("MALO")) {
            Alarma_libro alarma = new Alarma_libro();
            Administracion administracion = new Administracion();
            Stock stock = new Stock();
            Compras compras = new Compras();
            alarma.attach(administracion);
            alarma.attach(stock);
            alarma.attach(compras);

            alarma.notifyObservers();
        }
    }
}