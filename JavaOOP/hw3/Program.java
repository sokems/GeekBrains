import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;

import figures.*;

public class Program extends AddFigure {
    public static void getCircleLength(List<Figure> figures) {
        for (Figure figure : figures) {
            if (figure instanceof CircleLengther) {
                System.out.printf("CircleLength: %.2f\n", ((CircleLengther) figure).CircleLength());
            }   
        }
    }

    public static void getPerimeters(List<Figure> figures) {
        for (Figure figure : figures) {
            if (figure instanceof Perimeter) {
                System.out.printf("perimeter: %.2f\n", ((Perimeter) figure).getPerimeter());
            }            
        }
    }

    public static void getAreys(List<Figure> figures) {
        for (Figure figure : figures) {
            System.out.printf("square: %.2f\n", figure.getArey());
        }
    }

    public static void addNew(List<Figure> figures) {
        System.out.print("1. Круг\n2. Квадрат\n3. Треугольник\n4. Прямоугольник\nКакую фигуру вы хотите добавить: ");
        Scanner iScanner = new Scanner(System.in);
        int addNewFigure = iScanner.nextInt();
            if (addNewFigure == 1) {
                System.out.print("Введите радиус круга: ");
                int radius = iScanner.nextInt();
                figures.add(AddFigure(radius));
                System.out.println(figures);
            } 
            else if (addNewFigure == 2) {
                System.out.print("Введите длину стороны: ");
                int sideSquare = iScanner.nextInt();
                figures.add(AddFigure(sideSquare, sideSquare));
                System.out.println(figures);
            } 
            else if (addNewFigure == 3) {
                System.out.print("Введите длину стороны 1: ");
                int sideTriangle1 = iScanner.nextInt();
                System.out.print("Введите длину стороны 2: ");
                int sideTriangle2 = iScanner.nextInt();
                System.out.print("Введите длину стороны 3: ");
                int sideTriangle3 = iScanner.nextInt();
                figures.add(AddFigure(sideTriangle1, sideTriangle2, sideTriangle3));
                System.out.println(figures);
            } 
            else if (addNewFigure == 4) {
                System.out.print("Введите длину стороны 1: ");
                int sideRectangle1 = iScanner.nextInt();
                System.out.print("Введите длину стороны 2: ");
                int sideRectangle2 = iScanner.nextInt();
                figures.add(AddFigure(sideRectangle1, sideRectangle1, sideRectangle2, sideRectangle2));
                System.out.println(figures);
            } 
    }

    public static void showFigure(List<Figure> figures) {
        int count = 1;
        System.out.println();
        for (Figure figure : figures) {
            System.out.printf("%d. ", count);
            System.out.println(figure);
            count++;
        }
    }

    public static void deleteFigure(List<Figure> figures) {
        System.out.print("\nВведите номер фигуры, которую вы хотите удалить: ");
        try {
            Scanner iScanner = new Scanner(System.in);
            int num = iScanner.nextInt(); 
            figures.remove(num - 1);
            System.out.print("Фигура удалена из списка\n");
        } catch (Exception e) {
            System.out.print("Фигуры с таким номером не существует!\n");
        }
    }

    public static void replaceFigure(List<Figure> figures) {
        System.out.print("\nВведите номер фигуры, которую вы хотите заменить: ");
        try {
            Scanner iScanner = new Scanner(System.in);
            int num = iScanner.nextInt();
            System.out.print("1. Круг\n2. Квадрат\n3. Треугольник\n4. Прямоугольник\nКакую фигуру вы хотите добавить: ");
            int addNewFigure = iScanner.nextInt();
            if (addNewFigure == 1) {
                System.out.print("Введите радиус круга: ");
                int radius = iScanner.nextInt();
                figures.set(num - 1, AddFigure(radius));
            } 
            else if (addNewFigure == 2) {
                System.out.print("Введите длину стороны: ");
                int sideSquare = iScanner.nextInt();
                figures.set(num - 1, AddFigure(sideSquare, sideSquare));
            } 
            else if (addNewFigure == 3) {
                System.out.print("Введите длину стороны 1: ");
                int sideTriangle1 = iScanner.nextInt();
                System.out.print("Введите длину стороны 2: ");
                int sideTriangle2 = iScanner.nextInt();
                System.out.print("Введите длину стороны 3: ");
                int sideTriangle3 = iScanner.nextInt();
                figures.set(num - 1, AddFigure(sideTriangle1, sideTriangle2, sideTriangle3));
            } 
            else if (addNewFigure == 4) {
                System.out.print("Введите длину стороны 1: ");
                int sideRectangle1 = iScanner.nextInt();
                System.out.print("Введите длину стороны 2: ");
                int sideRectangle2 = iScanner.nextInt();
                figures.set(num - 1, AddFigure(sideRectangle1, sideRectangle1, sideRectangle2, sideRectangle2));
            }  
            System.out.print("Готово!\n");
        } catch (Exception e) {
            System.out.print("Фигуры с таким номером не существует!\n");
        }
    }
    
    public static void sortFigure(List<Figure> figures) {
        Collections.sort(figures);
        showFigure(figures);
    }

    public static void main(String[] args) {
        boolean exit = true;
        List<Figure> figures = new ArrayList<Figure>();
        Scanner iScanner = new Scanner(System.in);
        while (exit) {
            System.out.println();
            System.out.println("1. Добавить новую фигуру\n2. Вывести всю информацию о фигурах");
            System.out.println("3. Удалить фигуру\n4. Изменить фигуру по ндексу");
            System.out.println("5. Сортировка по площади и вывод информации о всех фигурах");
            System.out.println();
            System.out.print("Что будем делать: ");
            int menu = iScanner.nextInt();
            if (menu == 1) addNew(figures);
            else if (menu == 2) showFigure(figures);
            else if (menu == 3) deleteFigure(figures);
            else if (menu == 4) replaceFigure(figures);
            else if (menu == 5) sortFigure(figures);
            else exit = false;
        }
    }
}