package figures;

public abstract class Figure implements Comparable<Figure> {
    public abstract double getArey();

    @Override
    public int compareTo(Figure o) {
        if (this.getArey() > o.getArey())
            return 1;
        else if (this.getArey() < o.getArey())
            return -1;
        else
            return 0;
    }
}