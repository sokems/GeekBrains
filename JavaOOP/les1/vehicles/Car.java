package vehicles;

public class Car extends Vehicle{
    private String fuel;

    public Car(String color, String model, int wheelCount, double weight, double speed, String fuel) {
        super(color, model, wheelCount, weight, speed);
        this.fuel = fuel;
    }

    @Override
    public void drive(){
        System.out.println("Driving car");
    }


}
