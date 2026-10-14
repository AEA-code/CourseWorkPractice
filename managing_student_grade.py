
students = ["Alice","Ben","Chloe","Ama"]
for student in students:
    print(student)

#break statement
while True:
    grade = input("Enter the grade (type 'done' to finish): ")
    if grade.lower() == "done":  # Allows 'DONE', 'Done', etc.
        break
    print(f"Grade recorded: {grade}")


print("Done!")
  

# continues statement
while True:
    grade = input("Enter the grade: ")
    if grade < "0":
        continue
  
  
classes = [["Alice", "Ben"], ["Chloe", "David"]]

for first in classes:
    for second in first:
        print(first,"->",second)
  
  
  
# Using break to stop the program  
while True:
    grade = int(input("Enter the students grade: "))
    if grade < 0:
        break
  
  
#using continue to skip invalid imput
while True:
    grade = int(input("Enter the students grade: "))
    if grade < 0:
        continue
print("Enter next grade and it should non negative integer.")



# Stop the program when invalid input is entered
while True:
    grade = int(input("Enter the student's grade : "))

    # Stop entering grades completely
    if grade < 0:
        print("Grade entry stopped.")
        break

# Skip invalid input when it is entered    
while True:
    grade = int(input("Enter the student's grade : "))
    # Skip invalid grades
    if grade < 0:
        print("Invalid grade. Skipping...")
        continue




classes = [["Alice", "Ben"], ["Chloe", "David"]]

for i, class_group in enumerate(classes, start=1):
    for student in class_group:
        print(f"Class {i} -> {student}")




while True:
    try:
        grade_input = input("Enter the student's grade (type 'done' to stop): ")
    
        # Stop entering grades completely
        if grade_input.lower() == "done":
            print("Grade entry stopped.")
            break
    
        grade = int(grade_input)
    
        # Skip invalid grades
        if grade < 0:
            print("Invalid grade. Skipping...")
            continue
    except ValueError:
        print("Enter only numeric digit")







        