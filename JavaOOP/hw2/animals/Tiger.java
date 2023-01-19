package animals;

public class Tiger extends WildAnimal {

    public Tiger(String height, String weight, String colorEyes, String habitat, String dateLocation) {
        super(height, weight, colorEyes, habitat, dateLocation);
    }

    @Override
    public void getSound() {
        System.out.println("Арррр");
    }

    @Override
    public void getInfo() {
        
    }

    @Override
    public String toString() {
        return String.format("height: %s, weight: %s, colorEyes: %s, habitat: %s, dateLocation: %s", height, weight, colorEyes, habitat, dateLocation);
    }
    
}
