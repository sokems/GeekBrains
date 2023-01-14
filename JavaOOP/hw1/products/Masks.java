package products;

public class Masks extends Hygiene {
    public Masks(String name, double price, int count, String unit, int piecesPerPack) {
        super(name, price, count, unit, piecesPerPack);
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, pieces per pack: %d", 
        getName(), getPrice(), getCount(), getUnit(), getPiecesPerPack());
    }
}
