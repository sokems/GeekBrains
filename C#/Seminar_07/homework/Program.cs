// Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.

double[,] CreateRandom2dArray(int row, int column, double minValue, double maxValue)
{
    double[,] array = new double[row, column];
    for(int i = 0; i < row; i++)
        for(int j = 0; j < column; j++)
        {
            array[i, j] = new Random().NextDouble()*(maxValue - minValue) + minValue;
            array[i, j] = Math.Round(array[i, j], 2);
        }
    return array;
}

void Show2dArray(double[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j]);
            Console.Write(" ");
        }
        Console.WriteLine();
    }
}

Console.Write("Введите количество строк в массиве: ");
int row = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов в массиве: ");
int column = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите минимально допустимое число: ");
int minValue = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите максимально допустимое число: ");
int maxValue = Convert.ToInt32(Console.ReadLine());
Console.WriteLine();

double[,] array = CreateRandom2dArray(row, column, minValue, maxValue);
Show2dArray(array);


// Напишите программу, которая на вход принимает позиции элемента в двумерном массиве,
// и возвращает значение этого элемента или же указание, что такого элемента нет.

int[,] CreateRandom2dArray(int row, int column, int minValue, int maxValue)
{
    int[,] array = new int[row, column];
    for(int i = 0; i < row; i++)
        for(int j = 0; j < column; j++)
            array[i, j] = new Random().Next(minValue, maxValue + 1);
    return array;
}

void Show2dArray(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j]);
            Console.Write(" ");
        }
        Console.WriteLine();
    }
}

void FindElement(int[,] array, int i, int j)
{
    if((i <= array.GetLength(0)) && (j <= array.GetLength(1)))
        Console.WriteLine($"Элемент с заданными индексами равен {array[i - 1, j - 1]}.");
    else Console.WriteLine("Элемента с заданными индексами не существует!");
}

Console.Write("Введите количество строк в массиве: ");
int row = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов в массиве: ");
int column = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите минимально допустимое число: ");
int minValue = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите максимально допустимое число: ");
int maxValue = Convert.ToInt32(Console.ReadLine());
Console.WriteLine();

int[,] array = CreateRandom2dArray(row, column, minValue, maxValue);
Show2dArray(array);
Console.WriteLine();

Console.Write("Введите номер строки (счет от 1): ");
int numberRow = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите номер столбца (счет от 1): ");
int numberColumn = Convert.ToInt32(Console.ReadLine());
FindElement(array, numberRow, numberColumn);


// Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.

int[,] CreateRandom2dArray(int row, int column, int minValue, int maxValue)
{
    int[,] array = new int[row, column];
    for(int i = 0; i < row; i++)
        for(int j = 0; j < column; j++)
            array[i, j] = new Random().Next(minValue, maxValue + 1);
    return array;
}

void Show2dArray(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write(array[i, j]);
            Console.Write(" ");
        }
        Console.WriteLine();
    }
}

void MeanArithmeticColumn(int[,] array)
{
    for(int j = 0; j < array.GetLength(1); j++)
    {
        double meanArithmetic = 0;
        for(int i = 0; i < array.GetLength(0); i++)
            meanArithmetic += array[i, j];
        meanArithmetic /= array.GetLength(0);
        meanArithmetic = Math.Round(meanArithmetic, 2);
        Console.WriteLine($"Среднее арифметическое {j + 1} столбца равно {meanArithmetic}");
    }
}

Console.Write("Введите количество строк в массиве: ");
int row = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов в массиве: ");
int column = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите минимально допустимое число: ");
int minValue = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите максимально допустимое число: ");
int maxValue = Convert.ToInt32(Console.ReadLine());
Console.WriteLine();

int[,] array = CreateRandom2dArray(row, column, minValue, maxValue);
Show2dArray(array);
Console.WriteLine();
MeanArithmeticColumn(array);