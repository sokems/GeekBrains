public class program5 {

    public static void formatter(int counter, char ch) {
        if (counter != 1) {
            System.out.printf("%s%d", ch, counter);
        } else {
            System.out.printf("%s", ch);
        } 
    }
    
    public static void main(String[] args) {
        String orig = "aaaabbbcddeeaavqq";
        int counter = 1;
        for (int i = 0; i < orig.length() - 1; i++) {
            if (orig.charAt(i) == orig.charAt(i + 1)) {
                counter++;
            } else {
                formatter(counter, orig.charAt(i));
                counter = 1;
            }
        }
        formatter(counter, orig.charAt(orig.length() - 1));
    }
}

