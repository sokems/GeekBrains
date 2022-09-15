// Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.

int SumValue(int m, int n)
{
    if(n < m)
    {
        if(m > n) return SumValue(m - 1, n) + m;
        else return m;
    }
    else
    {        
        if(n > m) return SumValue(m, n - 1) + n;
        else return n;
    }
}

Console.Write("Введите первое число: ");
int numberFirst = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите второе число: ");
int numberSecond = Convert.ToInt32(Console.ReadLine());
Console.WriteLine();
if(numberFirst < numberSecond) 
    Console.WriteLine($"Сумма натуральных элементов в промежутке от {numberFirst} до {numberSecond} равна {SumValue(numberFirst, numberSecond)}");
else
    Console.WriteLine($"Сумма натуральных элементов в промежутке от {numberSecond} до {numberFirst} равна {SumValue(numberFirst, numberSecond)}");


// Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.

int FunctionAck(int m, int n)
{
    if(m == 0) return n + 1;
    if((m > 0) && (n == 0)) return FunctionAck(m - 1, 1);
    if((m > 0) && (n > 0)) return FunctionAck(m - 1, FunctionAck(m, n - 1));
    else return n + 1;
}

Console.Write("Введите первое число: ");
int numFirst = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите второе число: ");
int numSecond = Convert.ToInt32(Console.ReadLine());
Console.WriteLine();
Console.WriteLine($"Результат вычислений функции Аккермана чисел {numFirst} и {numSecond} равен {FunctionAck(numFirst, numSecond)}");