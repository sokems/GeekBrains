/* Вычислить n-ое треугольного число(сумма чисел от 1 до n), n! (произведение чисел от 1 до n) */

import java.util.Scanner;

public class ex1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Введите число n: ");
        int num = in.nextInt();
        in.close();
        int triang = 0;
        int fact = 1;
        for (int i = 1; i <= num; i++) {
            triang += i;
            fact *= i;
        }
        System.out.printf("%d-e треугольное число равно %d\n", num, triang);
        System.out.printf("Факториал числа %d равен %d", num, fact);
    }
}