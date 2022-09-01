// Напишите программу, которая принимает на вход число (А) и выдаёт сумму чисел от 1 до А.

// int FindSum(int num)
// {
//     int sum = 0;

//     for(int current = 1; current <= num; current++)
//     {
//         sum += current;
//     }

//     return sum;
// }

// Console.Write("Введите число: ");
// int a = Convert.ToInt32(Console.ReadLine());

// Console.WriteLine(FindSum(a));

// Напишите программу, которая принимает на вход число и выдаёт количество цифр в числе.

// int FindSum(int num)
// {
//     int sum = 0;
//     for (int current = 1; current <= num; current ++)
//         sum += current;
//     return sum;
// }
// Console.Write("Input positive integer number: ");
// int a = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine($"Sum of numbers from 1 to {a} is {FindSum(a)}");

// Напишите программу, которая принимает на вход число N и выдаёт произведение чисел от 1 до N.

// int AmountOfNumbers(int number)
// {
//     int current = number;
//     int output = 0;
//     while (current > 0)
//     {
//         current = current / 10;
//         output ++;
//     }
//     return output;
// }
// Console.Write("Input your number: ");
// int num = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine(AmountOfNumbers(num));

// Напишите программу, которая выводит массив из 8 элементов, заполненный нулями и единицами в случайном порядке.

// int FindFact(int num)
// {
//     int sum = 1;
//     for (int current = 1; current <= num; current ++)
//         sum *= current;
//     return sum;
// }
// Console.Write("Input positive integer number: ");
// int a = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine($"Sum of numbers from 1 to {a} is {FindFact(a)}");


// Напишите программу, которая выводит массив из 8 элементов, заполненный нулями и единицами в случайном порядке.

void FillArray(int[] collection)
{
    int length = collection.Length;

    for(index = 0; index < length; index++)
    {
        collection[index] = new Random().Next(0, 2);
    }

}

void PrintArray(int[] col)
{
    int count = col.Length;

    for(position = 0; position < count; position++)
    {
        Console.Write(col[position] + " ");
    }
}

int[] array = new int[8];

FillArray(array);
PrintArray(array);
