package products;

public class ToiletPaper extends Hygiene {
    private int countLayers;

    public ToiletPaper(String name, double price, int count, String unit, int piecesPerPack, int countLayers) {
        super(name, price, countLayers, unit, piecesPerPack);
        this.countLayers = countLayers;
    }

    public int getCountLayers() {
        return this.countLayers;
    }

    @Override
    public String toString() {
        return String.format("name: %s, price: %f, count: %d, unit: %s, pieces per pack: %d, count layers: %d", 
        getName(), getPrice(), getCount(), getUnit(), getPiecesPerPack(), getCountLayers());
    }
}
