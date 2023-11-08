package Pack_Observer;

public class Stock implements Libro_Mal_Estado{
    @Override
    public void update() {
        System.out.println("Stock: ");
        System.out.println("El libro salio de stock");
    }
}
