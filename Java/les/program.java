import java.time.LocalDateTime;
import java.util.Scanner;

public class program {
    public static void main(String[] args) {
        System.out.println(LocalDateTime.now());
        Scanner in = new Scanner(System.in);
        System.out.print("Введите имя: ");
        String name = in.nextLine();
        System.out.printf("Привет %s", name);
        in.close();
    }
}