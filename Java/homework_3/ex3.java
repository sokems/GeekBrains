import java.util.ArrayList;
import java.util.Arrays;

public class ex3 {
    public static void main(String[] args) {
        ArrayList <Integer> list = new ArrayList<>(Arrays.asList(5, 4, 7, 2, 3, 1, 6, 2));
        System.out.println(list);
        int maxValue = list.get(list.size() - 1);
        int minValue = list.get(0);
        float middleValue = 0;
        for(int item: list) {
            if (item > maxValue) maxValue = item;
            else if (item < minValue) minValue = item;
            middleValue += item;
        }
        middleValue /= list.size();
        System.out.printf("MaxValue = %d \nMinValue = %d \nMiddleValue = %f", maxValue, minValue, middleValue);
    }
}
