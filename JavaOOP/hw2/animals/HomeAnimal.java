package animals;

public abstract class HomeAnimal extends Animal {
    public String name;
    public String breed;
    public String vaccination;
    public String colorBody;
    public String birthday;

    public HomeAnimal(String height, String weight, String colorEyes, String name, String breed, String vaccination, String colorBody, String birthday){
        super(height, weight, colorEyes);
        this.name = name;
        this.breed = breed;
        this.vaccination = vaccination;
        this.colorBody = colorBody;
        this.birthday = birthday;
    }

    public abstract void love();
}
