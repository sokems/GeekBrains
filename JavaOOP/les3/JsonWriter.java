public class JsonWriter<E> {
    public String saveJson(E element) {
        if (element instanceof String) {
            return String.format("\"%s\"", (String) element) ;
        }
        else if (element instanceof Integer) {
            return element.toString();
        }
        else {
            return String.format("{ \"height\": %d, \"weight\": %d, \"colorEyes\": \"%s\" }", 
            ((Cat) element).height, ((Cat) element).weight, ((Cat) element).colorEyes);
        }
    }
}
