/* Дано четное число N (>0) и символы c1 и c2. Написать метод, который вернет строку длины N, 
которая состоит из чередующихся символов c1 и c2, начиная с c1.
 */

import java.util.Scanner;

public class program4 {
    public static void main(String[] args) {
        int check = 0;
        Scanner in = new Scanner(System.in);
        while (check == 0) {
            System.out.print("Введите число N: ");
            int n = in.nextInt();
            String res = "";
            if ((n % 2) == 0) {
                check = 1;
                for (int i = 2 ; i <= n; i += 2) {
                    res += "c1 c2 ";
                }
                System.out.print(res);
            } else {
                System.out.println("Введите четное число!");
            }
        }
        in.close();
    }
}
