package products;

public class Diapers extends Kids{
    private String size;
    private int minWeight;
    private int maxWeight;
    private String type;

    public Diapers(String name, double price, int count, String unit, int minAge, 
    String hypoallergenic, String size, int minWeight, int maxWeight, String type) {
        super(name, price, count, unit, minAge, hypoallergenic);
        this.size = size;
        this.minWeight = minWeight;
        this.maxWeight = maxWeight;
        this.type = type;
    }

    public int getMinWeight() {
        return this.minWeight;
    }

    public int getMaxWeight() {
        return this.maxWeight;
    }

    public String getSize() {
        return this.size;
    }

    public String getType() {
        return this.type;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, minimum age: %d, hypoallergenic: %s, minWeight: %d, maxWeight: %d, size: %s, type: %s", 
        getName(), getPrice(), getCount(), getUnit(), getMinAge(), getHypoallergenic(), getMinWeight(), getMaxWeight(), getSize(), getType());
    }
}
