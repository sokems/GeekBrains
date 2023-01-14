import java.util.List;
import products.*;

public class Main {
    public static void main(String[] args) {
        Product food = new Food("Snickers", 76, 1, "piece", "2025 year");
        Product bread = new Bread("GoodBread", 26, 2, "piece", "2023 year", "wheat flour");
        Product eggs = new Eggs("ChickenEggs", 60, 1, "piece", "2023 year", 10);
        Product drink = new Drink("Water", 23, 5, "piece", 0.5);
        Product lemonade = new Lemonade("LemonWater", 52, 2, "piece", 0.5);
        Product milk = new Milk("FunMilk", 36, 1, "piece", 0.95, 3.2, "2023 year");
        Product hygiene = new Hygiene("Soap", 5, 3, "piece", 3);
        Product masks = new Masks("CharcoalMasks", 120, 1, "piece", 10);
        Product toiletPaper = new ToiletPaper("Zeva", 150, 1, "piece", 6, 3);
        Product kids = new Kids("KidsFood", 578, 1, "piece", 1, "Yes");
        Product dummy = new Dummy("TastyDummy", 1200, 1, "piece", 0, "Yes");
        Product diapers = new Diapers("Huggies", 3200, 1, "piece", 0, "Yes", "2", 5, 8, "EliteSoft");

        List<Product> products = List.of(food, bread, eggs, drink, lemonade, milk, hygiene, masks, toiletPaper, kids, dummy, diapers);
        for(Product element : products){
            Program.printData(element);
        }
    }
}
