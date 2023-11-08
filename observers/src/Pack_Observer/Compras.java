package Pack_Observer;

public class Compras implements Libro_Mal_Estado{
    @Override
    public void update() {
        System.out.println("Compras: ");
        System.out.println("Enviando compra de libro");
    }
}
