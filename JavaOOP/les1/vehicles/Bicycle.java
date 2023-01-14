package vehicles;

public class Bicycle extends Vehicle {

    public Bicycle(String color, String model, int wheelCount, double weight, double speed) {
        super(color, model, wheelCount, weight, speed);
    }

    @Override
    public void drive(){
        System.out.println("Driving bicycle");
    }
}
