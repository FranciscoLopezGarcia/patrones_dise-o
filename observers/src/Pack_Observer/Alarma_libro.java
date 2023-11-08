package Pack_Observer;

import java.util.ArrayList;

public class Alarma_libro implements Subject{

    private ArrayList<Libro_Mal_Estado> observers = new ArrayList<Libro_Mal_Estado>();
    @Override
    public void attach(Libro_Mal_Estado observer) {
        observers.add(observer);

    }

    @Override
    public void detach(Libro_Mal_Estado observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for (Libro_Mal_Estado observer : observers) {
            observer.update();
        }

    }
}
