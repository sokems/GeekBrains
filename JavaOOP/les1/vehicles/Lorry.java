package vehicles;

public class Lorry extends Vehicle {

    public Lorry(String color, String model, int wheelCount, double weight, double speed) {
        super(color, model, wheelCount, weight, speed);
    }

    @Override
    public void drive(){
        System.out.println("Driving lorry");
    }
}
