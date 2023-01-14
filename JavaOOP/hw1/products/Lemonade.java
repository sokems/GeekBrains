package products;

public class Lemonade extends Drink {
    public Lemonade(String name, double price, int count, String unit, double volume){
        super(name, price, count, unit, volume);
    }
    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, volume: %f", getName(), getPrice(), getCount(), getUnit(), getVolume());
    }
}
