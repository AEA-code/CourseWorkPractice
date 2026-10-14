print("===== STUDENT GRADE MANAGER =====")

Students = [
    ["Ali", [85, 90, 78]],
    ["Sara", [92, 88, 95]],
    ["John", [55, 60, 48]],
    ["Maya", [70, 75, 80]]
]

while True:
    print("\nEnter your choice:")
    print("1) Show students")
    print("2) Add student")
    print("3) Show averages")
    print("4) Show top student")
    print("5) Show pass or fail")
    print("6) search for student")
    print("7) Exist")

    choice = input("Choice: ")

    if choice == "1":
        print("\nStudents:")
        for name, grades in Students:
            print(name, grades)

    elif choice == "2":
        print("\nAdd student")
        print("Enter student name and 3 grades separated by spaces:")

        a, b, c, d = input().split()

        b = int(b)
        c = int(c)
        d = int(d)

        Students.append([a, [b, c, d]])

        print("Student added successfully!")

    elif choice == "3":
        print("\nStudent averages:")

        for name, grades in Students:
            total = sum(grades)
            avg = total / len(grades)

            print(f"{name}: Total = {total}, Average = {avg:.2f}")

    elif choice == "4":
        max_average = 0
        top_student = ""

        for name, grades in Students:
            average = sum(grades) / len(grades)

            if average > max_average:
                max_average = average
                top_student = name

        print()
        print(f"Top student is {top_student} with Average {max_average:.2f}")

    elif choice == "5":
        print("\nPass or Fail:")
        passed=0

        for name, grades in Students:
            avg = sum(grades) / len(grades)

            if avg >= 60:
                print(f"{name} -> {avg:.2f} -> Pass")
                passed+=1
            else:
                print(f"{name} -> {avg:.2f} -> Fail")
                
        print(f"Only {passed} students Pass:")
        
    elif choice=="6":
        search=input("Name of student: ")
        for search,number in Students:
            print(search)
        if search not in Students[0]:
            print("Name not found")
        else:
            continue
            
    elif choice == "7":
        print("Program closed")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

        
    # Students.reverse() 
    # print(Students)
    # The number of students that Pass
   
        
        
        
        
        
        
        
        
        
        
        