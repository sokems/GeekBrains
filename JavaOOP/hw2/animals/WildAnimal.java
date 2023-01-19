package animals;

public abstract class WildAnimal extends Animal {
    public String habitat;
    public String dateLocation;

    public WildAnimal(String height, String weight, String colorEyes, String habitat, String dateLocation) {
        super(height, weight, colorEyes);
        this.habitat = habitat;
        this.dateLocation = dateLocation;
    }
}