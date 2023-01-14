package products;

public class Eggs extends Food {
    private int piecesPerPack;

    public Eggs(String name, double price, int count, String unit, String expirationDate, int piecesPerPack) {
        super(name, price, count, unit, expirationDate);
        this.piecesPerPack = piecesPerPack;
    }

    public int getPiecesPerPack() {
        return this.piecesPerPack;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, expiration date: %s, pieces per pack: %s", 
        getName(), getPrice(), getCount(), getUnit(), getExpDate(), getPiecesPerPack());
    }
}
