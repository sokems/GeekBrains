// Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.

/*
void SecondNum(int num)
{
    if(num > 99 && num < 1000)
    {
        int secondNumber = (num % 100) / 10;
        Console.WriteLine($"Вторая цифра вашего числа {secondNumber}");
    }
    else Console.WriteLine("Введите трёхзначное число!");
}

Console.WriteLine("Введите трёхзначное число.");
int number = Convert.ToInt32(Console.ReadLine());
SecondNum(number);
*/

// Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.

/*
void ThirdNum(int num)
{
    if(num < 100) Console.WriteLine("Третьей цифры нет!");
    if(num < 1000 && num > 100)
    {
        Console.WriteLine($"Третья цифра {num % 10}");
    }
    if(num > 999)
    {
        while(num > 999)
        {
            num = num / 10;
        }
    
    Console.WriteLine($"Третья цифра {num % 10}");
    }
}

Console.Write("Введите число: ");
int number = Convert.ToInt32(Console.ReadLine());
ThirdNum(number);
*/

// Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

void Weekend(int day)
{
    if(day > 7 || day < 1) Console.WriteLine("Введите число от 1 по 7!");
    if(day == 6 || day == 7) Console.WriteLine($"{day} день является выходным.");
    if(day > 0 && day < 6) Console.WriteLine($"{day} - будни");
}

Console.Write("Введите число (день недели): ");
int number = Convert.ToInt32(Console.ReadLine());
Weekend(number);