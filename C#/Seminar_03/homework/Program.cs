// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.

// void PolyNum(int num)
// {
//     int firstNum = num / 10000;
//     int secondNum = (num / 1000) % 10;
//     int fourthNum = (num % 100) / 10;
//     int fifthNum = num % 10;

//     if(((firstNum) == (fifthNum)) && ((secondNum) == (fourthNum)))
//     {
//         Console.WriteLine("Ваше число является палиндромом.");
//     }
//     else 
//     { 
//         Console.WriteLine("Ваше число НЕ является палиндромом.");
//     }
// }

// Console.Write("Введите число: ");
// int Number = Convert.ToInt32(Console.ReadLine());
// PolyNum(Number);


// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.

// void Distance(double xA, double yA, double zA, double xB, double yB, double zB)
// {
//     double dist = Math.Sqrt(Math.Pow((xA - xB), 2) + Math.Pow((yA - yB), 2) + Math.Pow((zA - zB), 2));
//     Console.WriteLine($"Растояние между точками ({xA},{yA},{zA}) и ({xB},{yB},{zB}) равно {dist}");
// }

// Console.WriteLine("Введите координаты точки А.");

// Console.Write("x = ");
// double xA = Convert.ToDouble(Console.ReadLine());
// Console.Write("y = ");
// double yA = Convert.ToDouble(Console.ReadLine());
// Console.Write("z = ");
// double zA = Convert.ToDouble(Console.ReadLine());
// Console.WriteLine();

// Console.WriteLine("Введите координаты точки B.");

// Console.Write("x = ");
// double xB = Convert.ToDouble(Console.ReadLine());
// Console.Write("y = ");
// double yB = Convert.ToDouble(Console.ReadLine());
// Console.Write("z = ");
// double zB = Convert.ToDouble(Console.ReadLine());
// Console.WriteLine();

// Distance(xA, yA, zA, xB, yB, zB);


// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.

void CubeNum(int num)
{
    int current = 1;
    if(num > 0)
    {
        while(current <= num)
        {
            Console.Write($"{Math.Pow(current, 3)} ");
            current++;
        }
    }
    else Console.WriteLine("Введите число больше 0!");
}

Console.Write("Введите число: ");
int num = Convert.ToInt32(Console.ReadLine());
CubeNum(num);