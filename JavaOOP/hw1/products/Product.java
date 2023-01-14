package products;

public class Product {
    private String name;
    private double price;
    private int count;
    private String unit;

    public Product(String name, double price, int count, String unit) {
        this.name = name;
        this.price = price;
        this.count = count;
        this.unit = unit;
    }

    public String getName() {
        return this.name;
    }

    public double getPrice() {
        return this.price;
    }

    public int getCount() {
        return this.count;
    }

    public String getUnit() {
        return this.unit;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s", getName(), getPrice(), getCount(), getUnit());
    }
}
