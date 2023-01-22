import figures.*;

public class AddFigure {
    public static Figure AddFigure(double element) {
        Figure circle = new Cicle(element);
        return circle;
    }

    public static Figure AddFigure(double element, double element_2) {
        Figure square = new Square(element, element_2);
        return square;
    }

    public static Figure AddFigure(double element, double element_2, double element_3) {
        Figure triangle = new Triangle(element, element_2, element_3);
        return triangle;
    }

    public static Figure AddFigure(double element, double element_2, double element_3, double element_4) {
        Figure rectangle = new Rectangle(element, element_2, element_3, element_4);   
        return rectangle;
    }
}
