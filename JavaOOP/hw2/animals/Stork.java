package animals;

public class Stork extends Bird {

    public Stork(String height, String weight, String colorEyes, String heightFly) {
        super(height, weight, colorEyes, heightFly);
    }

    @Override
    public void getSound() {
        System.out.println("Ау");
    }

    @Override
    public void getInfo() {
        
    }
    
}
