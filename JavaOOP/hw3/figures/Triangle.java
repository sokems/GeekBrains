package figures;

public class Triangle extends Polygon {
    public Triangle(double side1, double side2, double side3) {
        super(new double[]{side1, side2, side3});
    }

    @Override
    public double getArey() {
        double p = this.getPerimeter() / 2;
        double side1 = this.sides[0];
        double side2 = this.sides[1];
        double side3 = this.sides[2];
        double square = Math.sqrt(p * (p - side1) * (p - side2) * (p - side3));
        return square;
    }  
    
    @Override
    public String toString() {
        return String.format("Треугольник. Сторона 1: %f, Сторона 2: %f, Сторона 3: %f, Периметр: %f, Площадь: %f", 
        this.sides[0], this.sides[1], this.sides[2], this.getPerimeter(), this.getArey());
    }
}
