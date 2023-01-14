package products;

public class Drink extends Product{
    private double volume;

    public Drink(String name, double price, int count, String unit, double volume){
        super(name, price, count, unit);
        this.volume = volume;
    }

    public double getVolume() {
        return this.volume;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, volume: %f", getName(), getPrice(), getCount(), getUnit(), getVolume());
    }
}
