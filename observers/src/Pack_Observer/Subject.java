package Pack_Observer;

public interface Subject {
    void attach(Libro_Mal_Estado observer);
    void detach(Libro_Mal_Estado observer);
    void notifyObservers();
    }

