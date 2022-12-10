/* Вывести все простые числа от 1 до 1000 */

public class ex2 {
    public static void main(String[] args) {
        boolean check = false;
        for (int i = 1; i < 1000; i++) {
            for (int j = 2; j < i; j++) {
                if ((i % j == 0) && (i != j)) {
                    check = true;
                }
            }
            if (check == false) System.out.printf("| %d ", i);
            check = false;
        }
    }
}
