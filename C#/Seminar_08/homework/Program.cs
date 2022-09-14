// Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.

// int[,] NewRandom2dArray(int row, int column, int minValue, int maxValue)
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
//         for(int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j]);
//             Console.Write(' ');
//         }
//         Console.WriteLine();
//     }
// }

// void SortValueColumns(int[,] array)
// {
//     for(int i = 0; i < array.GetLength(0); i++)
//         for(int j = 0; j < array.GetLength(1) - 1; j++)
//         {
//             for(int k = j + 1; k < array.GetLength(1); k++)
//             {
//                 if(array[i, j] < array[i, k])
//                 {
//                     int temp = array[i, j];
//                     array[i, j] = array[i, k];
//                     array[i, k] = temp;
//                 }
//             }
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

// int[,] array = NewRandom2dArray(row, column, minValue, maxValue);
// Show2dArray(array);
// Console.WriteLine();
// SortValueColumns(array);
// Show2dArray(array);


// Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

// int[,] NewRandom2dArray(int row, int column, int minValue, int maxValue)
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
//         for(int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j]);
//             Console.Write(' ');
//         }
//         Console.WriteLine();
//     }
// }

// void MinSumValues(int[,] array)
// {
//     int minSumRow = 0;
//     int minSum = 0;

//     for(int i = 1; i < array.GetLength(0); i++)
//     {
//         int sumSecond = 0;
//         for(int j = 0; j < array.GetLength(1); j++)
//         {
//             if(i == 1)
//                 minSum += array[i - 1, j];
//             sumSecond += array[i, j];
//         }
//         if(sumSecond < minSum)
//         {
//             minSum = sumSecond;
//             minSumRow = i;
//         }
//     }
//     Console.Write($"Наименьшая сумма элементов в {minSumRow + 1} строчке.");
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

// int[,] array = NewRandom2dArray(row, column, minValue, maxValue);
// Show2dArray(array);
// Console.WriteLine();
// MinSumValues(array);


// Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.

// int[,] NewRandom2dArray(int row, int column, int minValue, int maxValue)
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
//         for(int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write(array[i, j]);
//             Console.Write(' ');
//         }
//         Console.WriteLine();
//     }
// }

// bool CheckMultiArray(int[,] arrayFirst, int[,] arraySecond)
// {
//     bool check = false;
//     if(arrayFirst.GetLength(1) == arraySecond.GetLength(0))
//         check = true;
//     return check;
// }

// int[,] MultiArray(int[,] arrayFirst, int[,] arraySecond)
// {
//     int[,] multiArray = new int[arrayFirst.GetLength(0), arraySecond.GetLength(1)];
//     for(int i = 0; i < arrayFirst.GetLength(0); i++)
//         for(int j = 0; j < arraySecond.GetLength(1); j++)
//             for(int n = 0; n < arrayFirst.GetLength(1); n++)
//                 multiArray[i, j] += arrayFirst[i, n] * arraySecond[n, j];
   
//     return multiArray;
// }

// Console.Write("Введите количество строк 1 матрицы: ");
// int row1 = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество столбцов 1 матрицы: ");
// int column1 = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество строк 2 матрицы: ");
// int row2 = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество столбцов 2 матрицы: ");
// int column2 = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите минимально допустимое число: ");
// int minValue = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите максимально допустимое число: ");
// int maxValue = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine();

// Console.WriteLine(" 1 матрица:");
// int[,] array1 = NewRandom2dArray(row1, column1, minValue, maxValue);
// Show2dArray(array1);
// Console.WriteLine();
// Console.WriteLine(" 2 матрица:");
// int[,] array2 = NewRandom2dArray(row2, column2, minValue, maxValue);
// Show2dArray(array2);
// Console.WriteLine();
// if(CheckMultiArray(array1, array2))
// {
//     Console.WriteLine(" Произведение матриц равно ");
//     int[,] array = MultiArray(array1, array2);
//     Show2dArray(array);
// }
// else
//     Console.WriteLine("Матрицы нельзя перемножить!");


// Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
// Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.

// int[,,] CreateRandom3dArray(int row, int column, int plane)
// {
//     int[,,] array = new int[row, column, plane];
    
//     for(int i = 0; i < row; i++)
//         for(int j = 0; j < column; j++)
//         {
//             int k = 0;
//             while(k < plane)
//             {
//                 int number = new Random().Next(10, 100);
//                 if(FindNumber(array, number)) continue;
//                 array[i, j, k] = number;
//                 k++;
//             }
//         }
//     return array;
// }

// bool FindNumber(int[,,] array, int number)
// {
//     bool findNumber = false;
//     for(int i = 0; i < array.GetLength(0); i++)
//         for(int j = 0; j < array.GetLength(1); j++)
//             for(int k = 0; k < array.GetLength(2); k++)
//             {
//                 if(array[i, j, k] == number)
//                     findNumber = true;
//             }
//     return findNumber;
// }

// void ShowValueWithIndexArray(int[,,] array)
// {
//     for(int i = 0; i < array.GetLength(0); i++)
//     {
//         for(int j = 0; j < array.GetLength(1); j++)
//         {
//             for(int k = 0; k < array.GetLength(2); k++)
//             {
//                 Console.Write($"{array[i, j, k]}({i},{j},{k}) ");
//             }
//             Console.WriteLine();
//         }
        
//     }
// }

// Console.Write("Введите количество строк в массиве: ");
// int row = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество столбцов в массиве: ");
// int column = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите количество плоскостей в массиве: ");
// int plane = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine();

// int[,,] array = CreateRandom3dArray(row, column, plane);
// ShowValueWithIndexArray(array);


// Напишите программу, которая заполнит спирально массив n на m.

int[,] CreateNullArray(int row, int column)
{
    int[,] array = new int[row, column];
    for(int i = 0; i < row; i++)
        for(int j = 0; j < column; j++)
        {
            array[i, j] = 0;
        }
    return array;
}

void ReadSpiralArray(int[,] array)
{
    int value = 01;
    int i = 0;
    int j = 0;

    for(int n = 0; n < array.GetLength(0)*array.GetLength(1); n++)
    {
        while(j < array.GetLength(1))
        {
            if(array[i, j] != 0) break;
            array[i, j] = value;
            value++;
            j++;
        }
        i++;
        j--;

        while(i < array.GetLength(0))
        {
            if(array[i, j] != 0) break;
            array[i, j] = value;
            value++;
            i++;
        }
        j--;
        i--;

        while(j >= 0)
        {
            if(array[i, j] != 0) break;
            array[i, j] = value;
            value++;
            j--;
        }
        j++;
        i--;

        while(i >= 0)
        {
            if(array[i, j] != 0) break;
            array[i, j] = value;
            value++;
            i--;
        } 
        i++;
        j++;  
    }
}

void Show2dArray(int[,] array)
{
    for(int i = 0; i < array.GetLength(0); i++)
    {
        for(int j = 0; j < array.GetLength(1); j++)
        {
            if(array[i, j] / 10 != 0)
                Console.Write(array[i, j]);
            else
                Console.Write($"0{array[i, j]}");
            Console.Write(' ');
        }
        Console.WriteLine();
    }
}

Console.Write("Введите количество строк в массиве: ");
int row = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите количество столбцов в массиве: ");
int column = Convert.ToInt32(Console.ReadLine());
Console.WriteLine();
int[,] array = CreateNullArray(row, column);
ReadSpiralArray(array);
Show2dArray(array);