// Задайте двумерный массив. Напишите программу, которая поменяет местами первую и последнюю строку массива.


// Задайте двумерный массив. Напишите программу, которая заменяет строки на столбцы. В случае, если это невозможно, программа должна вывести сообщение для пользователя.

// int[,] CreateRandom2dArray(int row, int column, int minValue, int maxValue)
// {
//     int[,] array = new int[row, column];
//     for(int i = 0; i < row; i++)
//         for(int j = 0; j < column; j++)
//         {
//             array[i, j] = new Random().Next(minValue, maxValue);
//         }
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

// void ReverseArray(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0) - 1; i++)
//         for(int j = i + 1; j < array.GetLength(1); j++)
//         {
//             int temp = array[i, j];
//             array[i, j] = array[j, i]; 
//             array[j, i] = temp;       
//         }
// }

// Console.Write("Введите количество строк в массиве: ");
// int row = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество столбцов в массиве: ");
// int column = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите минимально допустимое число: ");
// int minValue = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите максимально допустимое число: ");
// int maxValue = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine();

// int[,] array = CreateRandom2dArray(row, column, minValue, maxValue);
// Show2dArray(array);
// Console.WriteLine();
// ReverseArray(array);
// Show2dArray(array);


// Из двумерного массива целых чисел удалить строку и столбец, на пересечении которых расположен наименьший элемент.

int[,] CreateRandom2dArray(int row, int column, int minValue, int maxValue)
{
    int[,] array = new int[row, column];
    for(int i = 0; i < row; i++)
        for(int j = 0; j < column; j++)
        {
            array[i, j] = new Random().Next(minValue, maxValue);
        }
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

void DeleteMinValueRowColumn(int[,] array)
{
    int iMin = 0;
    int jMin = 0;

    for(int i = 0; i < array.GetLength(0); i++)
        for(int j = 0; j < array.GetLength(1); j++)
        {
            if(array[i, j] < array[iMin, jMin])
                {
                    iMin = i;
                    jMin = j;
                } 
        }

    for(int i = 0; i < array.GetLength(0); i++)
        for(int j = 0; j < array.GetLength(1); j++)
        {
            if((i == iMin) || (j == jMin))
                {
                    array[i, j] = 0;
                }        
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
DeleteMinValueRowColumn(array);
Show2dArray(array);


// Написать программу поэлементного копирования массива.

// int[,] CreateRandom2dArray(int row, int column, int minValue, int maxValue)
// {
//     int[,] array = new int[row, column];
//     for(int i = 0; i < row; i++)
//         for(int j = 0; j < column; j++)
//         {
//             array[i, j] = new Random().Next(minValue, maxValue);
//         }
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

// int[,] CreateCopyFirstArray(int[,] array)
// {
//     int[,] newArray = new int[array.GetLength(0), array.GetLength(1)];
//     for(int i = 0; i < array.GetLength(0); i++)
//         for(int j = 0; j < array.GetLength(1); j++)
//         {
//             newArray[i, j] = array[i,j];
//         }
//     return newArray;
// }

// Console.Write("Введите количество строк в массиве: ");
// int row = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество столбцов в массиве: ");
// int column = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите минимально допустимое число: ");
// int minValue = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите максимально допустимое число: ");
// int maxValue = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine();

// int[,] array = CreateRandom2dArray(row, column, minValue, maxValue);
// Show2dArray(array);
// Console.WriteLine();
// int[,] newArray = CreateCopyFirstArray(array);
// Show2dArray(newArray);


