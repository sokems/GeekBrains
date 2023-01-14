package products;

public class Bread extends Food {
    private String typeOfFlour;

    public Bread(String name, double price, int count, String unit, String expirationDate, String typeOfFlour) {
        super(name, price, count, unit, expirationDate);
        this.typeOfFlour = typeOfFlour;
    }

    public String getTypeOfFlour() {
        return this.typeOfFlour;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, expiration date: %s, type of flour: %s", 
        getName(), getPrice(), getCount(), getUnit(), getExpDate(), getTypeOfFlour());
    }
}
