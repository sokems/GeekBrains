import java.io.FileNotFoundException;
import java.sql.Struct;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class sem_2 {
    public static void main(String[] args) {
        //task_2(new int[] {1,2,3});
        // task_2(null);
        //task_3();
        // task_4();
    }


    public static void task1() {
        //Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
        // и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению
        // приложения, вместо этого, необходимо повторно запросить у пользователя ввод данных.


        float num = 0;
        boolean run = true;
        while (run) {
            run = false;
            System.out.println("Введите дробное число");
            Scanner in = new Scanner(System.in);
            try {
                num = in.nextFloat();

            } catch (InputMismatchException e) {
                System.out.println("Вы ввели не число");
                run = true;
            } catch (NoSuchElementException e) {
                System.out.println("Ошибка сканера");
                run = true;
            } finally {
                // in.close();
            }
        }
        System.out.println("Введеное число " + num);
    }

    public static void task_2(int[] intArray) {
        try {
            int d = 0;
            double catchedRes1 = intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);


        } catch (NullPointerException e) {
            System.out.println("Передан пустой объект: " + e);
        } catch (ArithmeticException e) {
            System.out.println("Деление на О: " + e);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Выход за пределы массива: " + e);
        }


    }

    public static void task_3() {
        //throws Exception
        try {
            int a = 90;
            int b = 3;
            System.out.println(a / b);
            printSum(23, null);
            int[] abc = {1, 2};
            abc[3] = 9;
        } catch (NullPointerException ex) {
            System.out.println("Указатель не может указывать на null!");
        } catch (IndexOutOfBoundsException ex) {
            System.out.println("Массив выходит за пределы своего размера!");
        } catch (ArithmeticException e) {
            System.out.println("Деление на О: " + e);
        } catch (Throwable ex) {
            System.out.println("Что-то пошло не так...");
        }
    }

    public static void printSum(Integer a, Integer b) throws NullPointerException {
        System.out.println(a + b);

    }

    public static void task_4() {
        //Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
        // Пользователю должно показаться сообщение, что пустые строки вводить нельзя.

        System.out.println("Введите строку");
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();

        try {
            if (str.isEmpty()) throw new RuntimeException("пустые строки вводить нельзя");
        } catch (RuntimeException e) {
            System.out.println(e.getMessage());
        }
    }
}
