package vehicles;

public class Bike extends Vehicle {

    public Bike(String color, String model, int wheelCount, double weight, double speed) {
        super(color, model, wheelCount, weight, speed);
    }

    @Override
    public void drive(){
        System.out.println("Driving bike");
    }
}
