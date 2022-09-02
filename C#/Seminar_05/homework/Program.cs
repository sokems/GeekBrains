// Задайте массив заполненный случайными положительными трёхзначными числами.
// Напишите программу, которая покажет количество чётных чисел в массиве.

int[] Array(int size)
{
    int[] array = new int[size];

    for(int i = 0; i < size; i++)
    {
        array[i] = new Random().Next(100, 1000);
    }

    return array;
}

void ShowArray(int[] array)
{
    int size = array.Length;

    for(int i = 0; i < size; i++)
    {
        if(i == 0) Console.Write($"[{array[i]}, ");
        if((i > 0) && (i < size - 1)) Console.Write($"{array[i]}, ");
        if(i == size - 1) Console.WriteLine($"{array[i]}]");
    }
}

int EvenNumbers(int[] array)
{
    int current = 0;
    int size = array.Length;
    for(int i = 0; i < size; i++)
    {
        if(array[i] % 2 == 0) current++;
    }

    return current;
}

Console.Write("Введите размер массива: ");
int sizeArray = Convert.ToInt32(Console.ReadLine());

int[] array = Array(sizeArray);
ShowArray(array);

Console.Write($"Четных чисел в массиве {EvenNumbers(array)}");


// Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.

int[] Array(int size, int min, int max)
{
    int[] array = new int[size];
    for(int i = 0; i < size; i++)
    {
        array[i] = new Random().Next(min, max);
    }

    return array;
}

void ShowArray(int[] array)
{
    int size = array.Length;

    for(int i = 0; i < size; i++)
    {
        if(i == 0) Console.Write($"[{array[i]}, ");
        if((i > 0) && (i < size - 1)) Console.Write($"{array[i]}, ");
        if(i == size - 1) Console.WriteLine($"{array[i]}]");
    }
}

int SumOddNumbers(int[] array)
{
    int size = array.Length;
    int sum = 0;
    for(int i = 0; i < size; i++)
    {
        if(i % 2 != 0) sum += array[i];
    }

    return sum;
}

Console.Write("Введите размер массива: ");
int sizeArray = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите нижнюю границу чисел: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите верхнюю границу чисел: ");
int max = Convert.ToInt32(Console.ReadLine());

int[] array = Array(sizeArray, min, max);
ShowArray(array);

Console.WriteLine($"Сумма элементов, стоящих на нечётных позициях равна {SumOddNumbers(array)}");


// Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.

double[] Array(int size)
{
    double[] array = new double[size];
    for(int i = 0; i < size; i++)
    {
        array[i] = new Random().NextDouble();
        array[i] = Math.Round(array[i], 3);
    }

    return array;
}

void ShowArray(double[] array)
{
    int size = array.Length;

    for(int i = 0; i < size; i++)
    {
        if(i == 0) Console.Write($"[{array[i]}, ");
        if((i > 0) && (i < size - 1)) Console.Write($"{array[i]}, ");
        if(i == size - 1) Console.WriteLine($"{array[i]}]");
    }

    Console.WriteLine();
}

double Min(double[] array)
{
    int size = array.Length;
    double min = array[0];
    for(int i = 1; i < size; i++)
    {
        if(array[i] < min) min = array[i];
    }

    return min;
}

double Max(double[] array)
{
    int size = array.Length;
    double max = array[0];
    for(int i = 1; i < size; i++)
    {
        if(array[i] > max) max = array[i];
    }

    return max;
}

Console.Write("Введите размер массива: ");
int sizeArray = Convert.ToInt32(Console.ReadLine());

double[] array = Array(sizeArray);
ShowArray(array);

Console.WriteLine($"Минимальный элемент: {Min(array)}. \nМаксимальный элемент: {Max(array)}");
Console.WriteLine($"Разница равна: {Max(array) - Min(array)}");