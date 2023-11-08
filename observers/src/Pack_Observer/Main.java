package Pack_Observer;

public class Main {

    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();
        Libro libro = new Libro("MALO", "El señor de los anillos");


        biblioteca.devolver_Libro(libro);
    }

}
