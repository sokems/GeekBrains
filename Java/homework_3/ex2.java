import java.util.ArrayList;
import java.util.Arrays;

public class ex2 {
    public static void main(String[] args) {
        ArrayList <Integer> list = new ArrayList<>(Arrays.asList(5, 4, 7, 2, 3, 1, 6, 2));
        ArrayList <Integer> listRes = new ArrayList<>();
        for(int item: list) {
            if (item % 2 != 0) {
                listRes.add(item);
            }
        }
        System.out.println(listRes);
    }
}
