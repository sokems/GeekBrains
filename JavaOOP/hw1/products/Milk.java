package products;

public class Milk extends Drink {
    private double fat;
    private String expirationDate;

    public Milk(String name, double price, int count, String unit, double volume, double fat, String expirationDate) {
        super(name, price, count, unit, volume);
        this.fat = fat;
        this.expirationDate = expirationDate;
    }

    public double getFat() {
        return this.fat;
    }

    public String getExpDate() {
        return this.expirationDate;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, volume: %f, fat: %f, expiration date: %s", 
        getName(), getPrice(), getCount(), getUnit(), getVolume(), getFat(), getExpDate());
    }
}
