import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import animals.*;

public class Zoo {

    public static void main(String[] args) {
        ArrayList<Animal> animalList = new ArrayList<Animal>();
        boolean flag = true;
        while (flag == true) {
            Scanner iScanner = new Scanner(System.in);
            System.out.print("\n1. Добавить животное\n2. Удалить животное\n3. Посмотреть информацию о конкретном животном\n4. Издать звук конкретное животное\n5. Посмотреть информацию обо всех животных\n6. Издать звук всем животным\n7. Выход\nЧто хотите сделать: ");
            int menu = iScanner.nextInt(); 
            if (menu == 1) addAnimal(animalList);
            else if (menu == 2) deleteAnimal(animalList);
            else if (menu == 3) getInfoAnimal(animalList);
            else if (menu == 4) getSoundAnimal(animalList);
            else if (menu == 5) getInfoAnimals(animalList);
            else if (menu == 6) getSoundAnimals(animalList);
            else flag = false;
        }
    }


    public static void getSoundAnimals(ArrayList list) {
        for (Object element : list) {
            String el = (String) element;
            if (el.startsWith("Ca")) {
                Animal cat = new Cat(null, null, null, null, null, null, null, null, null);
                cat.getSound();
            } else if (el.startsWith("Do")) {
                Animal dog = new Dog(null, null, null, null, null, null, null, null, null);
                dog.getSound();
            } else if (el.startsWith("Ti")) {
                Animal tiger = new Tiger(null, null, null, null, null);
                tiger.getSound();
            } else if (el.startsWith("Wo")) {
                Animal wolf = new Wolf(null, null, null, null, null, null);
                wolf.getSound();
            } else if (el.startsWith("Ch")) {
                Animal chicken = new Chicken(null, null, null, null);
                chicken.getSound();
            } else if (el.startsWith("St")) {
                Animal stork = new Stork(null, null, null, null);
                stork.getSound(); 
            }
        }
    }

    public static void getInfoAnimals(ArrayList list) {
        int count = 0;
        for (Object element : list) {
            System.out.printf("%d - %s\n", count, (String) element);
            count++;
        }
    }

    public static void getSoundAnimal(ArrayList list) {
        System.out.print("\nВведите номер животного: ");
        try {
            Scanner iScanner = new Scanner(System.in);
            int num = iScanner.nextInt(); 
            String element = (String) list.get(num);
            if (element.startsWith("Ca")) {
                Animal cat = new Cat(null, null, null, null, null, null, null, null, null);
                cat.getSound();
            } else if (element.startsWith("Do")) {
                Animal dog = new Dog(null, null, null, null, null, null, null, null, null);
                dog.getSound();
            } else if (element.startsWith("Ti")) {
                Animal tiger = new Tiger(null, null, null, null, null);
                tiger.getSound();
            } else if (element.startsWith("Wo")) {
                Animal wolf = new Wolf(null, null, null, null, null, null);
                wolf.getSound();
            } else if (element.startsWith("Ch")) {
                Animal chicken = new Chicken(null, null, null, null);
                chicken.getSound();
            } else if (element.startsWith("St")) {
                Animal stork = new Stork(null, null, null, null);
                stork.getSound();
            }

        } catch (Exception e) {
            System.out.print("Животного с таким номером не существует!\n");
        }
    }

    public static void getInfoAnimal(ArrayList list) {
        System.out.print("\nВведите номер животного: ");
        try {
            Scanner iScanner = new Scanner(System.in);
            int num = iScanner.nextInt(); 
            System.out.printf("%s\n", (String) list.get(num));
        } catch (Exception e) {
            System.out.print("Животного с таким номером не существует!\n");
        }
    }

    public static void deleteAnimal(ArrayList list) {
        System.out.print("\nВведите номер животного, которого вы хотите удалить: ");
        try {
            Scanner iScanner = new Scanner(System.in);
            int num = iScanner.nextInt(); 
            list.remove(num);
            System.out.print("Животного удалено из списка\n");
        } catch (Exception e) {
            System.out.print("Животного с таким номером не существует!\n");
        }
    }

    public static void addAnimal(ArrayList list) {
        System.out.print("\nКакого животного вы хотите добавить:\n1. Кошка\n2. Собака\n3. Тигр\n4. Волк\n5. Курица\n6. Аист\nВведите номер: ");
        Scanner iScanner = new Scanner(System.in);
        int typeAnimal = iScanner.nextInt();
        String res;
        if (typeAnimal == 1) {
            List<String> listAnimal = new ArrayList<>();
            listAnimal = addInfoAnimal();
            List<String> listHomeAnimal = new ArrayList<>();
            listHomeAnimal = addInfoHomeAnimal();
            List<String> listCat = new ArrayList<>();
            listCat = addInfoCat();
            Animal cat = new Cat(listAnimal.get(0), listAnimal.get(1), listAnimal.get(2), listHomeAnimal.get(0), 
            listHomeAnimal.get(1), listHomeAnimal.get(2), listHomeAnimal.get(3), listHomeAnimal.get(4), listCat.get(0));
            res = String.format("Cat. %s", cat);
            list.add(res);
        }
        else if (typeAnimal == 2) {
            List<String> listAnimal = new ArrayList<>();
            listAnimal = addInfoAnimal();
            List<String> listHomeAnimal = new ArrayList<>();
            listHomeAnimal = addInfoHomeAnimal();
            List<String> listDog = new ArrayList<>();
            listDog = addInfoDog();
            Animal dog = new Cat(listAnimal.get(0), listAnimal.get(1), listAnimal.get(2), listHomeAnimal.get(0), 
            listHomeAnimal.get(1), listHomeAnimal.get(2), listHomeAnimal.get(3), listHomeAnimal.get(4), listDog.get(0));
            res = String.format("Dog. %s", dog);
            list.add(res);
        }
        else if (typeAnimal == 3) {
            List<String> listAnimal = new ArrayList<>();
            listAnimal = addInfoAnimal();
            List<String> listWildAnimal = new ArrayList<>();
            listWildAnimal = addInfoWildAnimal();
            addInfo();
            Animal tiger = new Tiger(listAnimal.get(0), listAnimal.get(1), listAnimal.get(2), listWildAnimal.get(0), 
            listWildAnimal.get(1));
            res = String.format("Tiger. %s", tiger);
            list.add(res);
        }

        else if (typeAnimal == 4) {
            List<String> listAnimal = new ArrayList<>();
            listAnimal = addInfoAnimal();
            List<String> listWildAnimal = new ArrayList<>();
            listWildAnimal = addInfoWildAnimal();
            List<String> listWolf = new ArrayList<>();
            listWolf = addInfoWolf();
            Animal wolf = new Wolf(listAnimal.get(0), listAnimal.get(1), listAnimal.get(2), listWildAnimal.get(0), 
            listWildAnimal.get(1), listWolf.get(0));
            res = String.format("Wolf. %s", wolf);
            list.add(res);
        }

        else if (typeAnimal == 5) {
            List<String> listAnimal = new ArrayList<>();
            listAnimal = addInfoAnimal();
            List<String> listBird = new ArrayList<>();
            listBird = addInfoBird();
            addInfo();
            Animal chicken = new Chicken(listAnimal.get(0), listAnimal.get(1), listAnimal.get(2), listBird.get(0));
            res = String.format("Chicken. %s", chicken);
            list.add(res);
        }

        else if (typeAnimal == 6) {
            List<String> listAnimal = new ArrayList<>();
            listAnimal = addInfoAnimal();
            List<String> listBird = new ArrayList<>();
            listBird = addInfoBird();
            addInfo();
            Animal stork = new Stork(listAnimal.get(0), listAnimal.get(1), listAnimal.get(2), listBird.get(0));
            res = String.format("Stork. %s", stork);
            list.add(res);
        }
        else {
            System.out.println("Введено некорректное значение");
        }
    }

    public static List addInfoAnimal() {
        System.out.print("Введите рост: ");
        Scanner iScanner = new Scanner(System.in);
        String height = iScanner.nextLine();

        System.out.print("Введите вес: ");
        String weight = iScanner.nextLine();

        System.out.print("Введите цвет глаз: ");
        String colorEyes = iScanner.nextLine();

        List<String> list = List.of(height, weight, colorEyes);
        return list;
    }

        public static List addInfoHomeAnimal() {
            System.out.print("Введите кличку: ");
            Scanner iScanner1 = new Scanner(System.in);
            String name = iScanner1.nextLine();
    
            System.out.print("Введите породу: ");
            String breed = iScanner1.nextLine();
    
            System.out.print("Вакцинирован ли (да/нет): ");
            String vaccination = iScanner1.nextLine();

            System.out.print("Введите цвет шерсти: ");
            String colorBody = iScanner1.nextLine();

            System.out.print("Введите дату рождения: ");
            String birthday = iScanner1.nextLine();
    
            List<String> list = List.of(name, breed, vaccination, colorBody, birthday);
            return list;
        } 

        public static List addInfoWildAnimal() {
            System.out.print("Введите место обитания: ");
            Scanner iScanner1 = new Scanner(System.in);
            String habitat = iScanner1.nextLine();
    
            System.out.print("Введите дату нахождения: ");
            String dateLocation = iScanner1.nextLine();
    
            List<String> list = List.of(habitat, dateLocation);
            return list;
        } 

        public static List addInfoCat() {
            System.out.print("Есть ли шерсть (да/нет): ");
            Scanner iScanner2 = new Scanner(System.in);
            String presenceWool = iScanner2.nextLine();
    
            List<String> list = List.of(presenceWool);
            System.out.println("\nЖивотное добавлено!");
            return list;
        } 

        public static List addInfoDog() {
            System.out.print("Дрессировано (да/нет): ");
            Scanner iScanner2 = new Scanner(System.in);
            String training = iScanner2.nextLine();
    
            List<String> list = List.of(training);
            System.out.println("\nЖивотное добавлено!");
            return list;
        } 

        public static void addInfo() {
            System.out.println("\nЖивотное добавлено!");
        } 

        public static List addInfoWolf() {
            System.out.print("Вожак стаи (да/нет): ");
            Scanner iScanner2 = new Scanner(System.in);
            String lider = iScanner2.nextLine();
    
            List<String> list = List.of(lider);
            System.out.println("\nЖивотное добавлено!");
            return list;
        } 

        public static List addInfoBird() {
            System.out.print("Введите высоту полета: ");
            Scanner iScanner1 = new Scanner(System.in);
            String heightFly = iScanner1.nextLine();
    
            List<String> list = List.of(heightFly);
            return list;
        } 
    }
