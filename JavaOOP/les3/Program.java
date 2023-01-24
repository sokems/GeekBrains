public class Program {
    public static void main(String[] args) {
        Cat cat = new Cat(12, 20, "red");
        JsonWriter<Cat> catJson = new JsonWriter<>();
        JsonWriter<String> strJson = new JsonWriter<>();
        JsonWriter<Integer> intJson = new JsonWriter<>();

        WriteFile.createJsonFile("object", catJson.saveJson(cat));
        WriteFile.createJsonFile("String", strJson.saveJson("Строка"));
        WriteFile.createJsonFile("Integer", intJson.saveJson(123));

        ReadFile.readJsonFile("object");
    }
}
