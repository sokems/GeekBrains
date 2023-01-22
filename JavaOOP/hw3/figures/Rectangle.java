package figures;

public class Rectangle extends Polygon {
    
    public Rectangle(double length, double length2, double width, double width2) {
        super(new double[]{length, width, length, width});
    }

    @Override
    public double getArey() {
        return this.sides[0] * this.sides[1];
    }    

    @Override
    public String toString() {
        return String.format("Прямоугольник. Сторона 1: %f, Сторона 2: %f, Периметр: %f, Площадь: %f", 
        this.sides[0], this.sides[1], this.getPerimeter(), this.getArey());
    }
}
