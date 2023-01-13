/*
На языке Java реализовать следующий набор классов, при этом должна быть выделена их иерархия:
	2.1.Транспортное средство
	2.2.Автомобиль
	2.3.Мотоцикл
	2.4.Грузовик
	2.5.Велосипед
Во всех классах должны быть написаны: цвет, модель, количество колёс, вес и скорость а так же метод ехать.
В классе Program реализовать метод который будет работать с любым наследником класса ровно так же как и с родителем, 
то есть показать значение всех его публичных свойств и вызвать метод ехать.
 */

import java.util.List;
import vehicles.*;

public class Program {
    public static void main(String[] args) {
        Vehicle car = new Car("red", "BMW", 4, 1500, 240);
        Vehicle bike = new Bike("blue", "Yamaha", 2, 500, 300);
        Vehicle lorry = new Lorry("yellow", "Mersedes", 4, 3500, 100);
        Vehicle bicycle = new Bicycle("green", "Stels", 2, 10, 30);

        List<Vehicle> vehicles = List.of(car, bike, lorry, bicycle);
        for(Vehicle element : vehicles){
            printData(element);
        }
    }

    private static void printData(Vehicle element) {
        element.drive();
        System.out.println(element);
        System.out.println();
    }
}