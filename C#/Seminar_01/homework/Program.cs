// Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.

Console.WriteLine("   Задача №1");

Console.Write("Введите первое число: ");
int a = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите второе число: ");
int b = Convert.ToInt32(Console.ReadLine());

int maximum = a;
if (a < b)
{
    maximum = b;
    Console.WriteLine("a = " + a + "; b = " + b + " -> max = " + maximum);
}
else
{
    Console.WriteLine("a = " + a + "; b = " + b + " -> max = " + maximum);
}

Console.WriteLine();


// Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.

Console.WriteLine("   Задача №2");

Console.Write("Введите первое число: ");
int num_1 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите второе число: ");
int num_2 = Convert.ToInt32(Console.ReadLine());

Console.Write("Введите третье число: ");
int num_3 = Convert.ToInt32(Console.ReadLine());

int max = num_1;
if (num_1 < num_2)
{
    max = num_2;
}

if (max < num_3)
{
    max = num_3;
}

Console.WriteLine(num_1 + ", " + num_2 + ", " + num_3 + " -> " + max);

Console.WriteLine();


// Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).

Console.WriteLine("   Зачада №3");

Console.Write("Введите число: ");
int num = Convert.ToInt32(Console.ReadLine());

if (num % 2 == 0)
{
    Console.WriteLine(num + " -> да");
}
else
{
    Console.WriteLine(num + "-> нет");
}

Console.WriteLine();


// Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

Console.WriteLine("   Задача №4");

Console.Write("Ведите число: ");
int n = Convert.ToInt32(Console.ReadLine());
Console.Write(n + " -> ");

int current = 2;
while (current <= n)
{
    if (current % 2 == 0)
    {
        Console.Write(current + " ");
    }

    current++;
}

