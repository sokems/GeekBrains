/* Реализовать простой калькулятор */

import java.util.Scanner;
public class ex3 {
   public static void main(String[] args) {
      double num1;
      double num2;
      double ans;
      char op;
      Scanner reader = new Scanner(System.in);
      System.out.print("Введите 2 числа: ");
      num1 = reader.nextDouble();
      num2 = reader.nextDouble();
      System.out.print("\nВведите операцию (+, -, *, /): ");
      op = reader.next().charAt(0);
      switch(op) {
         case '+': ans = num1 + num2;
            break;
         case '-': ans = num1 - num2;
            break;
         case '*': ans = num1 * num2;
            break;
         case '/': ans = num1 / num2;
            break;
         default:  System.out.printf("Некоректный ввод");
            return;
      }
      System.out.print("\nРезультат:\n");
      System.out.printf(num1 + " " + op + " " + num2 + " = " + ans);
   }
}
