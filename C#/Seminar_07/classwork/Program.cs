// Задайте двумерный массив размером m×n, заполненный случайными целыми числами.

// int[,] Create2dArray(int row, int column, int minValue, int maxValue)
// {
//     int[,] array = new int[row, column];
//     for(int i = 0; i < row; i++)
//         for(int j = 0; j < column; j++)
//             array[i, j] = new Random().Next(minValue, maxValue + 1);
//     return array; 
// }

// void Show2dArray(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0); i++)
//     {
//                 for(int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j]);
//             Console.Write(" ");
//         }
//         Console.WriteLine();  
//     }

// }

// Console.Write("Введите количество строк в массиве: ");
// int row = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество столбцов в массиве: ");
// int column = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите минимально допустимое число: ");
// int minValue = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите максимально допустимое число: ");
// int maxValue = Convert.ToInt32(Console.ReadLine());

// int[,] array = Create2dArray(row, column, minValue, maxValue);
// Show2dArray(array);


// Задайте двумерный массив размера m на n, каждый элемент в массиве находится по формуле: Aij = i+j. Выведите полученный массив на экран.

// int[,] Create2dArray(int row, int column)
// {
//     int[,] array = new int[row, column];
//     for(int i = 0; i < row; i++)
//         for(int j = 0; j < column; j++)
//             array[i, j] = i + j;
//     return array;
// }

// void Show2dArray(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0); i++)
//     {
//         for(int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j]);
//             Console.Write(" ");
//         }
//         Console.WriteLine();
//     }
// }

// Console.Write("Введите количество строк: ");
// int row = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество стоблцов: ");
// int column = Convert.ToInt32(Console.ReadLine());
// int[,] array = Create2dArray(row, column);
// Show2dArray(array);


// Задайте двумерный массив. Найдите элементы, у которых оба индекса чётные, и замените эти элементы на их квадраты.

// int[,] CreateRandom2dArray(int row, int column, int minValue, int maxValue)
// {
//     int[,] array = new int[row, column];
//     for(int i = 0; i < row; i ++)
//         for(int j = 0; j < column; j++)
//             array[i, j] = new Random().Next(minValue, maxValue);
//     return array;
// }

// void Show2dArray(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0); i++)
//     {
//         for(int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j]);
//             Console.Write("  ");
//         }
//         Console.WriteLine();
//     }
// }

// void QuadEvenIndex(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0); i += 2)
//         for(int j = 0; j < array.GetLength(1); j += 2)
//             array[i, j] *= array[i, j];
// }

// Console.Write("Введите количество строк в массиве: ");
// int row = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество столбцов в массиве: ");
// int column = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите минимально допустимое число: ");
// int minValue = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите максимально допустимое число: ");
// int maxValue = Convert.ToInt32(Console.ReadLine());

// int[,] array = CreateRandom2dArray(row, column, minValue, maxValue);
// Show2dArray(array);
// Console.WriteLine();
// QuadEvenIndex(array);
// Show2dArray(array);


// Задайте двумерный массив. Найдите сумму элементов, находящихся на главной диагонали (с индексами (0,0); (1;1) и т.д.

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

int SumDiagValue(int[,] array)
{
    int sum = 0;
    for(int i = 0; i < array.GetLength(0) && i < array.GetLength(1); i++)
        sum += array[i, i];
    return sum;
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
Console.WriteLine($"Сумма элементов по главной диагонали равна {SumDiagValue(array)}");
