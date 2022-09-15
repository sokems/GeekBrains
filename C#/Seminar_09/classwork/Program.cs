// Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от 1 до N.

// void ShowNums(int n)
// {
//     if(n > 1) ShowNums(n - 1);
//     Console.Write(n + " ");
// }

// ShowNums(5);

// Напишите программу, которая будет принимать на вход число и возвращать сумму его цифр.

// int SumValues(int n)
// {
//     if(n > 0) return SumValues(n / 10) + (n % 10);
//     else return 0;
// }

// Console.WriteLine(SumValues(121));


// Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N.

void ShowNums(int m, int n)
{
    if(n > m)
    {
        if(n > m) ShowNums(m, n - 1);
        Console.Write(n + " ");
    }
    else
    {
        if(m > n) ShowNums(m, n + 1);
        Console.Write(n + " "); 
    }
}

ShowNums(10, 5);

// Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

int PowValue(int a, int b)
{
    if(b > 1) return PowValue(a, b - 1)*a;
    else return a;
}

Console.WriteLine(PowValue(2, 3));