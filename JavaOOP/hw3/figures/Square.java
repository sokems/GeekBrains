package figures;

public class Square extends Rectangle {
    public Square(double side, double sidecopy) {
        super(side, side, sidecopy, sidecopy);
    }

    @Override
    public String toString() {
        return String.format("Квадрат. Сторона: %f, Периметр: %f, Площадь: %f", 
        this.sides[0], this.getPerimeter(), this.getArey());
    }
}
