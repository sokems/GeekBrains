package figures;

public class Cicle extends Figure implements CircleLengther {
    protected double radius;

    public Cicle(double radius) {
        this.radius = radius;
    }

    @Override
    public double CircleLength() {
        return 2 * 3.14 * this.radius;
    }

    @Override
    public double getArey() {
        return 3.14 * this.radius * this.radius;
    }

    @Override
    public String toString() {
        return String.format("Круг. Радиус: %f, Длина окружности: %f, Площадь: %f", 
        this.radius, this.CircleLength(), this.getArey());
    }
    
}
