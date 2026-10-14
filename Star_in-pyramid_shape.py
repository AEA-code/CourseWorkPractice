
# Star pattern
# Printing star inpyramid shape

my_num = int(input("Enter the number: "))
for a in range(0,my_num):
    for b in range(0,my_num-a-1):
        print(end=" ")
    for c in range(0,a+1):
        print("*",end=" ")
    print()

print()
# Alphabet pattern

from string import ascii_uppercase
for i in range(1,27):
    print(" ".join(ascii_uppercase[:i]))

# Number pattern
num = int(input("Enter your number: "))
count = 1
for my_row in range(1,num+1):
    for my_col in range(1,my_row+1):
        print(count, end=" ")
    count +=1
    print()

# Exception handling 
# ZeroDivisionEror

print("string-1")

try:
    print(3/0)
    print("6/3",6/3)# not executed
except Exception as e:
    print("Normal Division")
    print("4/2=",4/2)
    print(e.__class__.__name__)
    print({e})

    
print("String-2")
print()
# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     total = num1 / num2
# except ValueError:
#     print("It is a value error: please enter an integer.")
# except ZeroDivisionError:
#     print("It is division by zero: cannot be divided by zero.")



