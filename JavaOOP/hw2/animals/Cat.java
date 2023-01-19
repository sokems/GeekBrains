package animals;

public class Cat extends HomeAnimal {
    public String presenceWool = "";

    public Cat(String height, String weight, String colorEyes, String name, String breed, String vaccination, 
    String colorBody, String birthday, String presenceWool) {
        super(height, weight, colorEyes, name, breed, vaccination, colorBody, birthday);
        this.presenceWool = presenceWool;
    }

    @Override
    public void getSound() {
        System.out.println("Мяу");
    }

    @Override
    public void getInfo() {
        System.out.printf("presenceWool: %s", presenceWool);
    }

    @Override
    public void love() {
        
    }

    @Override
    public String toString() {
        return String.format("height: %s, weight: %s, colorEyes: %s, name: %s, breed: %s, vaccination: %s, colorBody: %s, birthday: %s, presenceWool: %s", height, weight, colorEyes,  name, breed, vaccination, colorBody, birthday, presenceWool);
    }

    public String getPresenceWool() {
        return presenceWool;
    }

    public void setPresenceWool(String presenceWool) {
        this.presenceWool = presenceWool;
    }
}
