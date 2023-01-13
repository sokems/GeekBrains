package vehicles;

public class Lorry extends Vehicle {
    private String color;
    private String model;
    private int wheelCount;
    private double weight;
    private double speed;

    public Lorry(String color, String model, int wheelCount, double weight, double speed) {
        super(color, model, wheelCount, weight, speed);
    }

    @Override
    public void drive(){
        System.out.println("Driving lorry");
    }
}
