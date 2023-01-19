package animals;

public abstract class Animal {
    public String height;
    public String weight;
    public String colorEyes;

    public Animal(String height, String weight, String colorEyes) {
        this.height = height;
        this.weight = weight;
        this.colorEyes = colorEyes;
    }

    public abstract void getSound();
    public abstract void getInfo();
    
}