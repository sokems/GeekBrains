import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class ex1 {
    public static void main(String[] args) {
            Map<String, String> telBook = new HashMap<>();
        boolean exit = true;
        while (exit) {
            System.out.println("Что будем делать с телефонной книгой?\n1. Показать книгу\n2. Добавить запись\n3. Удалить запись\n4. Выход");
            Scanner iScanner = new Scanner(System.in);
            String inp = iScanner.nextLine();
            if (inp.equals("1")) {
                System.out.println(telBook);
            } else {
                if (inp.equals("2")) {
                    System.out.print("Введите Имя: ");
                    Scanner iScan = new Scanner(System.in);
                    String name = iScan.nextLine();
                    System.out.print("Введите номер телефона: ");
                    Scanner iScant= new Scanner(System.in);
                    String tel = iScant.nextLine();
                    telBook.put(name, tel);
                } else {
                    if (inp.equals("3")) {
                        System.out.print("Введите имя, которое хотите удалить: ");
                        Scanner iScan = new Scanner(System.in);
                        String name = iScan.nextLine();
                        telBook.remove(name);
                    } else {
                        if (inp.equals("4")) {
                            exit = false;
                            iScanner.close();
                        }
                        else {
                            System.out.println("Некоректный ввод!");
                        }
                    }
                }
            }  
            System.out.println();
        }
    }
}