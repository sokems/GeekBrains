package products;

public class Hygiene extends Product {
    private int piecesPerPack;

    public Hygiene(String name, double price, int count, String unit, int piecesPerPack) {
        super(name, price, count, unit);
        this.piecesPerPack = piecesPerPack;
    }

    public int getPiecesPerPack() {
        return this.piecesPerPack;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, pieces per pack: %d", 
        getName(), getPrice(), getCount(), getUnit(), getPiecesPerPack());
    }
}
