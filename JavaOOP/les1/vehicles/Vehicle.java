package vehicles;

/**
 * Во всех классах должны быть написаны: цвет, модель, количество колёс, вес и скорость а так же метод ехать.
 */
public class Vehicle {
    private String color;
    private String model;
    private int wheelCount;
    private double weight;
    private double speed;

    public Vehicle(String color, String model, int wheelCount, double weight, double speed) {
        this.color = color;
        this.model = model;
        this.wheelCount = wheelCount;
        this.weight = weight;
        this.speed = speed;
    }

    public void drive(){
        System.out.println("Base vehicle driving");
    }

    public String getColor() {
        return this.color;
    }

    public String getModel() {
        return this.model;
    }

    public int getWheelCount() {
        return this.wheelCount;
    }

    public double getWeight() {
        return this.weight;
    }

    public double getSpeed() {
        return this.speed;
    }

    @Override
    public String toString() {
        return String.format("color: %s, model: %s, wheelCount: %d, weight: %f, speed: %f", getColor(), getModel(), getWheelCount(), getWeight(), getSpeed());
    }
}