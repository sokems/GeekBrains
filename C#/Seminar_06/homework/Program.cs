// Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь. Решить без массива.

int Positive(int quan)
{
    int pos = 0;
    for(int i = 0; i < quan; i++)
    {
        Console.Write($"Введите {i + 1} число: ");
        int num = Convert.ToInt32(Console.ReadLine());
        if(num > 0) pos++;
    }

    return pos;
}

Console.Write("Введите количество чисел: ");
int quan = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"Количество положительных чисел равно {Positive(quan)}");

// Напишите программу, которая найдёт точку пересечения двух прямых, 
// заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.

double X_coord(double k1, double b1, double k2, double b2)
{
    double x = (b2 - b1) / (k1 - k2);
    return x;
}

Console.Write("Введите k1: ");
double k1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите b1: ");
double b1 = Convert.ToDouble(Console.ReadLine());
Console.WriteLine($"y = {k1} * x + {b1}");
Console.WriteLine();

Console.Write("Введите k2: ");
double k2 = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите b2: ");
double b2 = Convert.ToDouble(Console.ReadLine());
Console.WriteLine($"y = {k2} * x + {b2}");
Console.WriteLine();

if(k1 == k2) Console.WriteLine("Прямые параллельны!");
else Console.WriteLine($"Координаты точки пересечения: ({X_coord(k1, b1, k2, b2)}; {k1 * X_coord(k1, b1, k2, b2) + b1})");