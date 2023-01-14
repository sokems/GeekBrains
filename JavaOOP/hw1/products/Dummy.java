package products;

public class Dummy extends Kids {
    public Dummy(String name, double price, int count, String unit, int minAge, String hypoallergenic) {
        super(name, price, count, unit, minAge, hypoallergenic);
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, minimum age: %d, hypoallergenic: %s", 
        getName(), getPrice(), getCount(), getUnit(), getMinAge(), getHypoallergenic());
    }
}
