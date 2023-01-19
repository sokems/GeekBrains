package animals;

public class Chicken extends Bird {

    public Chicken(String height, String weight, String colorEyes, String heightFly) {
        super(height, weight, colorEyes, heightFly);
    }

    @Override
    public void getSound() {
        System.out.println("ко ко ко");
    }

    @Override
    public void getInfo() {
        
    }
    
}
