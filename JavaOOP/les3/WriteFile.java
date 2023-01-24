import java.io.File;
import java.io.FileWriter;
import java.io.IOException;


public class WriteFile {
    public static void createJsonFile(String name, String content)  {
        File file = new File(name + ".json");
        System.out.println(file.getAbsolutePath());
        try (FileWriter writer = new FileWriter(file)) {
            writer.write(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
