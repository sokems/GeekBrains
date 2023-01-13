package vehicles;

public class Car extends Vehicle{
    private String color;
    private String model;
    private int wheelCount;
    private double weight;
    private double speed;

    public Car(String color, String model, int wheelCount, double weight, double speed) {
        super(color, model, wheelCount, weight, speed);
    }

    @Override
    public void drive(){
        System.out.println("Driving car");
    }


}
