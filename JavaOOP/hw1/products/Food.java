package products;

public class Food extends Product {
    private String expirationDate;

    public Food(String name, double price, int count, String unit, String expirationDate) {
        super(name, price, count, unit);
        this.expirationDate = expirationDate;
    }

    public String getExpDate() {
        return this.expirationDate;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, expiration date: %s", getName(), getPrice(), getCount(), getUnit(), getExpDate());
    }
}
