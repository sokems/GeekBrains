package animals;

public class Wolf extends WildAnimal {
    public String lider = "";

    public Wolf(String height, String weight, String colorEyes, String habitat, String dateLocation, String lider) {
        super(height, weight, colorEyes, habitat, dateLocation);
        this.lider = lider;
    }

    @Override
    public void getSound() {
        System.out.println("Арррр");
    }

    @Override
    public void getInfo() {
        System.out.printf("lider: %s", lider);
    }

    @Override
    public String toString() {
        return String.format("height: %s, weight: %s, colorEyes: %s, habitat: %s, dateLocation: %s, lider: %s", height, weight, colorEyes, habitat, dateLocation, lider);
    }
}
