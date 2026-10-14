
# Storing students and their grades in four subjects
# Math, English, French and Science

Students = (
    ("Kofi", 30, 50, 68, 81),
    ("Ama", 86, 78, 70, 68),
    ("Emmanuel", 79, 71, 51, 45),
    ("Malik", 41, 50, 68, 73),
    ("Peter", 79, 61, 55, 89),
    ("Elolo", 100, 96, 95, 98)
)

while True:
    print("===== STUDENT MARKS MANAGER =====")
    print()
    print("The Menu System - Enter your choice:")
    print("1. Show all students")
    print("2. Search Student")
    print("3. Show highest Average")
    print("4. Show lowest Average")
    print("5. Show students who score above 80")
    print("6. Exit")
    print()

    choice = input("Choice: ")

    # 1. Show all students
    if choice == "1":
        print("\n===== ALL STUDENTS =====")

        for student in Students:
            print(student)

    # 2. Search Student
    elif choice == "2":
        studentname = input("Enter student name: ")

        found = False

        for student in Students:
            name = student[0]
            grades = student[1:]

            if studentname.lower() == name.lower():
                total = sum(grades)
                average = total / len(grades)

                print(f"\nStudent: {name}")
                print(f"Grades: {grades}")
                print(f"Total: {total}")
                print(f"Average: {average:.2f}")

                found = True
                break

        if not found:
            print("Invalid name")

    # 3. Show highest average
    elif choice == "3":
        highest_average = 0
        highest_student = ""

        for student in Students:
            name = student[0]
            grades = student[1:]

            total = sum(grades)
            average = total / len(grades)

            if average > highest_average:
                highest_average = average
                highest_student = name

        print()
        print(
            f"The student with the highest average is "
            f"{highest_student}, having an average of "
            f"{highest_average:.2f}"
        )

    # 4. Show lowest average
    elif choice == "4":
        lowest_average = float("inf")
        lowest_student = ""

        for student in Students:
            name = student[0]
            grades = student[1:]

            total = sum(grades)
            average = total / len(grades)

            if average < lowest_average:
                lowest_average = average
                lowest_student = name

        print()
        print(
            f"The student with the lowest average is "
            f"{lowest_student}, having an average of "
            f"{lowest_average:.2f}"
        )

    # 5. Show students with average >= 80
    elif choice == "5":
        print("\n===== STUDENTS WITH AVERAGE 80 OR ABOVE =====")

        found = False

        for student in Students:
            name = student[0]
            grades = student[1:]

            average = sum(grades) / len(grades)

            if average >= 80:
                print(f"{name}: {average:.2f}")
                found = True

        if not found:
            print("No student has an average of 80 or above.")

    # 6. Exit
    elif choice == "6":
        print("Program closed")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

    print()

