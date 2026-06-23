using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
namespace StudentManagementSystem
{
class Student
{
    public int Id { get; set; }
    public string Name { get; set; }
    public int Age { get; set; }

    public override string ToString()
    {
        return $"{Id},{Name},{Age}";
    }
}

class Program
{
    static List<Student> students = new List<Student>();
    static string filePath = "students.txt";

    static void Main()
    {
        LoadStudents();

        while (true)
        {
            Console.WriteLine("\n===== Student Management System =====");
            Console.WriteLine("1. Add Student");
            Console.WriteLine("2. View Students");
            Console.WriteLine("3. Search Student");
            Console.WriteLine("4. Delete Student");
            Console.WriteLine("5. Exit");

            Console.Write("Enter Choice: ");

            try
            {
                int choice = Convert.ToInt32(Console.ReadLine());

                switch (choice)
                {
                    case 1:
                        AddStudent();
                        break;

                    case 2:
                        ViewStudents();
                        break;

                    case 3:
                        SearchStudent();
                        break;

                    case 4:
                        DeleteStudent();
                        break;

                    case 5:
                        SaveStudents();
                        return;

                    default:
                        Console.WriteLine("Invalid Choice.");
                        break;
                }
            }
            catch
            {
                Console.WriteLine("Please enter a valid number.");
            }
        }
    }

    static void AddStudent()
    {
        try
        {
            Student student = new Student();

            Console.Write("Enter ID: ");
            student.Id = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter Name: ");
            student.Name = Console.ReadLine();

            Console.Write("Enter Age: ");
            student.Age = Convert.ToInt32(Console.ReadLine());

            students.Add(student);

            SaveStudents();

            Console.WriteLine("Student Added Successfully.");
        }
        catch
        {
            Console.WriteLine("Invalid Input.");
        }
    }

    static void ViewStudents()
    {
        if (students.Count == 0)
        {
            Console.WriteLine("No Students Available.");
            return;
        }

        foreach (Student student in students)
        {
            Console.WriteLine(
                $"ID: {student.Id}, Name: {student.Name}, Age: {student.Age}");
        }
    }

    static void SearchStudent()
    {
        try
        {
            Console.Write("Enter Student ID: ");

            int id = Convert.ToInt32(Console.ReadLine());

            var student = students.FirstOrDefault(s => s.Id == id);

            if (student != null)
            {
                Console.WriteLine(
                    $"Found: {student.Name}, Age: {student.Age}");
            }
            else
            {
                Console.WriteLine("Student Not Found.");
            }
        }
        catch
        {
            Console.WriteLine("Invalid Input.");
        }
    }

    static void DeleteStudent()
    {
        try
        {
            Console.Write("Enter Student ID: ");

            int id = Convert.ToInt32(Console.ReadLine());

            var student = students.FirstOrDefault(s => s.Id == id);

            if (student != null)
            {
                students.Remove(student);

                SaveStudents();

                Console.WriteLine("Student Deleted.");
            }
            else
            {
                Console.WriteLine("Student Not Found.");
            }
        }
        catch
        {
            Console.WriteLine("Invalid Input.");
        }
    }

    static void SaveStudents()
    {
        List<string> lines = new List<string>();

        foreach (var student in students)
        {
            lines.Add(student.ToString());
        }

        File.WriteAllLines(filePath, lines);
    }

    static void LoadStudents()
    {
        if (!File.Exists(filePath))
            return;

        var lines = File.ReadAllLines(filePath);

        foreach (var line in lines)
        {
            var data = line.Split(',');

            students.Add(new Student
            {
                Id = int.Parse(data[0]),
                Name = data[1],
                Age = int.Parse(data[2])
            });
        }
    }
}
}
