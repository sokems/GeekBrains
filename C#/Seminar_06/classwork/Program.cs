// Напишите программу, которая перевернёт одномерный массив (последний элемент будет на первом месте, а первый - на последнем и т.д.)

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

int[] Reverse(int[] array)
{
    for(int i = 0, j = array.Length - 1; i < j; i++, j--)
    {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    return array;
}

Console.Write("Введите размер массива: ");
int size = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите min: ");
int min = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите max: ");
int max = Convert.ToInt32(Console.ReadLine());

int[] array = Array(size, min, max);
ShowArray(array);
Reverse(array);
ShowArray(array);

// Напишите программу, которая принимает на вход три числа и проверяет, может ли существовать треугольник с сторонами такой длины.

// void Triang(int a, int b, int c)
// {
//     if((a < b + c) && (b < a + c) && (c < a + b)) Console.WriteLine("Треугольник существует.");
//     else Console.WriteLine("Треугольник НЕ существует.");
// }

// Console.Write("Введите 1 длину: ");
// int a = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите 2 длину: ");
// int b = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите 3 длину: ");
// int c = Convert.ToInt32(Console.ReadLine());
// Triang(a, b, c);

// Не используя рекурсию, выведите первые N чисел Фибоначчи. Первые два числа Фибоначчи: a и b.

// int[] Fibo(int a, int b, int size)
// {
//     int[] array = new int[size];
//     array[0] = a;
//     array[1] = b;
//     for(int i = 2; i < size; i++)
//     {
//         array[i] = array[i - 1] + array[i - 2];
//     }

//     return array;
// }

// void ShowArray(int[] array)
// {
//     int size = array.Length;

//     for(int i = 0; i < size; i++)
//     {
//         if(i == 0) Console.Write($"[{array[i]}, ");
//         if((i > 0) && (i < size - 1)) Console.Write($"{array[i]}, ");
//         if(i == size - 1) Console.WriteLine($"{array[i]}]");
//     }

//     Console.WriteLine();
// }

// Console.Write("Введите размер ряда: ");
// int size = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите 1 число: ");
// int a = Convert.ToInt32(Console.ReadLine());
// Console.Write("Введите 2 число: ");
// int b = Convert.ToInt32(Console.ReadLine());
// ShowArray(Fibo(a, b, size));

// Напишите программу, которая будет преобразовывать десятичное число в двоичное.

// string Duo(int num)
// {
//     string duo = string.Empty;
//     while(num > 0)
//     {
//         duo = num % 2 + duo;
//         num /= 2;
//     }
    
//     return duo;
// }

// Console.Write("Введите число: ");
// int num = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine(Duo(num));