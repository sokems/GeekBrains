import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class ReadFile {
    public static String readJsonFile(String name)  {
        File file = new File(name + ".json");
        String res = "";
        try (FileReader reader = new FileReader(file)) {
            int c;
            while ((c = reader.read()) != -1) 
                res += (char) c;
                return res;
        } catch (IOException e) {
            e.printStackTrace();
            return res;
        }
    }
}

