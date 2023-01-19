package animals;

public class Dog extends HomeAnimal {
    public String training = "";

    public Dog(String height, String weight, String colorEyes, String name, String breed, String vaccination, String colorBody, String birthday, String training) {
        super(height, weight, colorEyes, name, breed, vaccination, colorBody, birthday);
        this.training = training;
    }

    public void train() {

    }

    @Override
    public void getSound() {
        System.out.println("Гав");
    }

    @Override
    public void getInfo() {
        System.out.printf("training: %s", training);
    }

    @Override
    public void love() {
        
    }

    @Override
    public String toString() {
        return String.format("height: %s, weight: %s, colorEyes: %s, name: %s, breed: %s, vaccination: %s, colorBody: %s, birthday: %s, training: %s", height, weight, colorEyes, name, breed, vaccination, colorBody, birthday, training);
    }
}
