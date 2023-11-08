package Pack_Observer;

public class Administracion implements Libro_Mal_Estado{
    @Override
    public void update() {
        System.out.println("Administracion: ");
        System.out.println("El libro esta en mal estado, se debe pagar multa");
    }
}
