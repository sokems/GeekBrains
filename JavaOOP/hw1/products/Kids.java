package products;

public class Kids extends Product {
    private int minAge;
    private String hypoallergenic;

    public Kids(String name, double price, int count, String unit, int minAge, String hypoallergenic) {
        super(name, price, count, unit);
        this.minAge = minAge;
        this.hypoallergenic = hypoallergenic;
    }

    public int getMinAge() {
        return this.minAge;
    }

    public String getHypoallergenic() {
        return this.hypoallergenic;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, minimum age: %d, hypoallergenic: %s", 
        getName(), getPrice(), getCount(), getUnit(), getMinAge(), getHypoallergenic());
    }
}
