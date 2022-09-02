// Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.

// int DelSecondValue(int num)
// {
//     int firstValue = num / 100;
//     int thirdValue = num % 10;
//     int result = firstValue * 10 + thirdValue;
//     return result;
// }

// int number = new Random().Next(100, 999);
// Console.WriteLine($"Случайное число: {number} \nУдаляем вторую цифру: {DelSecondValue(number)}");


// Напишите программу, которая будет принимать на вход два числа и выводить, является ли второе число кратным первому. 
// Если второе число не кратно числу первому, то программа выводит остаток от деления.

void Multi(int num1, int num2)
{
    int ost = num2 % num1;
    if(ost == 0) Console.WriteLine($"Число {num2} кратно числу {num1}.");
    else 
    {
    
        Console.WriteLine($"Число {num2} НЕ кратно числу {num1}. \nОстаток от деления равен {ost}.");

    }
}

Console.Write("Введите 1 число: ");
int number1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите 2 число: ");
int number2 = Convert.ToInt32(Console.ReadLine());

Multi(number1, number2);




