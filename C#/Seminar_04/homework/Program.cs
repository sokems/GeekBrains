// Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.

// int Pow(int numA, int numB)
// {
//     int pow = numA;
//     for(int i = 2; i <= numB; i++)
//     {
//         pow *= numA;
//     }

//     return pow;
// }

// Console.Write("Введите число, которое нужно возвести в степень: ");
// int number = Convert.ToInt32(Console.ReadLine());

// Console.Write("Введите степень: ");
// int power = Convert.ToInt32(Console.ReadLine());

// Console.WriteLine($"{number} в степени {power} будет равно {Pow(number, power)}");



// Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.

// int SumValue(int number)
// {
//     int sum = 0;
//     int rem = number;
//     int value = number;

//     while(rem != 0)
//     {
//         rem %= 10;
//         sum += rem;
//         value /= 10;
//         rem = value;
//     }

//     return sum;
// }

// Console.Write("Введите число: ");
// int num = Convert.ToInt32(Console.ReadLine());

// Console.WriteLine($"Сумма цифр числа {num} равна {SumValue(num)}");



// Напишите программу, которая задаёт массив из N элементов и выводит их на экран.


void ReadMass(int[] array)
{
    int length = array.Length;
    for(int i = 0; i < length; i++)
    {
        Console.Write($"Введите {i+1} число: ");
        array[i] = Convert.ToInt32(Console.ReadLine());
    }

    Console.WriteLine();
}

void PrintMass(int[] arr)
{
    int count = arr.Length;
    int c = count - 1;
    Console.Write("Ваш массив: ");
    for(int i = 0; i < count; i++)
    {
        if(i == 0) Console.Write("[" + arr[i] + ", ");
        if(i == c) Console.Write(arr[i] + "]");
        if((i != 0) && (i != c)) Console.Write(arr[i] + ", ");
    }
}

Console.Write("Введите размер массива: ");
int len = Convert.ToInt32(Console.ReadLine());

int[] mass = new int[len];
ReadMass(mass);
PrintMass(mass);
