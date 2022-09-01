// Напишите программу замена элементов массива: положительные элементы замените на соответствующие отрицательные, и наоборот.

// int[] ReadMass(int[] array)
// {
//     int length = array.Length;
//     for(int i = 0; i < length; i++)
//     {
//         Console.Write($"Введите {i+1} число: ");
//         array[i] = Convert.ToInt32(Console.ReadLine());
//     }

//     Console.WriteLine();
//     return array;
// }

// void PrintMass(int[] arr)
// {
//     int count = arr.Length;
//     int c = count - 1;
//     Console.Write("Ваш массив: ");
//     for(int i = 0; i < count; i++)
//     {
//         if(i == 0) Console.Write("[" + arr[i] + ", ");
//         if(i == c) Console.Write(arr[i] + "]");
//         if((i != 0) && (i != c)) Console.Write(arr[i] + ", ");
//     }
// }

// int[] Replace(int[] array)
// {
//     int size = array.Length;
//     for(int i = 0; i < size; i++)
//     {
//         array[i] = -array[i];
//     }

//     return array;
    
// }

// Console.Write("Введите размер массива: ");
// int len = Convert.ToInt32(Console.ReadLine());

// int[] mass = new int[len];
// ReadMass(mass);
// PrintMass(mass);
// Replace(mass);
// Console.WriteLine();
// PrintMass(mass);

// Задайте массив. Напишите программу, которая определяет, присутствует ли заданное число в массиве.

// int[] ReadMass(int[] array, int max, int min)
// {
//     int length = array.Length;
//     for(int i = 0; i < length; i++)
//     {
//         array[i] = new Random().Next(min, max + 1);
//     }

//     Console.WriteLine();
//     return array;
// }

// void PrintMass(int[] arr)
// {
//     int count = arr.Length;
//     int c = count - 1;
//     Console.Write("Ваш массив: ");
//     for(int i = 0; i < count; i++)
//     {
//         if(i == 0) Console.Write("[" + arr[i] + ", ");
//         if(i == c) Console.Write(arr[i] + "]");
//         if((i != 0) && (i != c)) Console.Write(arr[i] + ", ");
//     }
// }

// bool FindValue(int[] array, int value)
// {
//     bool result = false;
//     int size = array.Length;
//     for(int i = 0; i < size; i++)
//     {
//         if(array[i] == value) result = true;
//     }
    
//     return result;
// }


// Console.Write("Введите размер массива: ");
// int len = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите max: ");
// int max = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите min: ");
// int min = Convert.ToInt32(Console.ReadLine());

// int[] mass = new int[len];
// ReadMass(mass, max, min);
// PrintMass(mass);
// Console.WriteLine();

// Console.Write("Введите число: ");
// int value = Convert.ToInt32(Console.ReadLine());

// if(FindValue(mass, value)) Console.Write("Число есть в массиве!");
// else Console.Write("Числа нет в массиве!");

// Задайте одномерный массив из 12 случайных чисел. Найдите количество элементов массива, значения которых лежат в отрезке [10,99].

int[] ReadMass(int[] array, int max, int min)
{
    int length = array.Length;
    for(int i = 0; i < length; i++)
    {
        array[i] = new Random().Next(min, max + 1);
    }

    Console.WriteLine();
    return array;
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

int FindValue(int[] array)
{
    int sum = 0;
    int size = array.Length;
    for(int i = 0; i < size; i++)
    {
        if((array[i] >= 10) && (array[i] <= 99)) sum++;
    }
    
    return sum;
}


Console.Write("Введите размер массива: ");
int len = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите max: ");
int max = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите min: ");
int min = Convert.ToInt32(Console.ReadLine());

int[] mass = new int[len];
ReadMass(mass, max, min);
PrintMass(mass);
Console.WriteLine();

Console.WriteLine($"Количество двухзначных чисел равно {FindValue(mass)}");