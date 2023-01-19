package animals;

public abstract class Bird extends Animal {
    protected String heightFly;



    public void fly(String heightFly) {
        System.out.printf("Я лечу на %d метрах", this.heightFly);
    }
    
    public Bird(String height, String weight, String colorEyes, String heightFly) {
        super(heightFly, weight, colorEyes);
        this.heightFly = heightFly;
    }
    
}
