import java.util.Arrays;
import java.util.LinkedList;

public class ex1 {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<Integer>(Arrays.asList(5, 4, 7, 2, 3, 1, 6, 2));

    for(int i = 0, mid = list.size()/2, j = list.size() - 1; i < mid; i++, j--) {
        list.set(i, list.set(j, list.get(i)));
        }
        System.out.println(list);
    }
}