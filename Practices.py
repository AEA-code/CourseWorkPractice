# # """A program that allow the user to guess the correct out between 1 through 10"""
# # choice = 9 #    the number the comouter pick
# # print("Pease guess a number between 1 and 10")
# # playerchoice = int(input())  #user prompt
# # if choice == playerchoice:
# #     print("You win") # out true if the 
# # else:
# #     print("sorry, you lose")




# # #A Rock-paper-scissor game 
# # choice = "paper" # computer choice
# # print("Rock-paper-scissor: type in your choice: ")
# # player = input().lower() # player input and convert to lower case if not

# # if player == "rock" and choice == "paper":
# #     print("sorry-computer win, try again.")

# # elif player == "scissor" and choice == "paper":
# #     print("sorry-computer win, try again.")

# # elif player == "paper" and choice == "rock":
# #     print("sorry-computer win, try again.")
# # else:
# #     print("congratulation 🎊, you won")
# #     # If player seelection not in rock,paper and scissor, out put error
# # if player not in "rock,paper,scissor":
# #     print("Error: Select one of: rock,paper,scissors")


# # for i in range(0,65):
# #     print(i,2**i)

# # print(2**64 * 2**64)

# # z = 1.2
# # if type(z) == float:
# #     print("true")
# # else:
# #     print("false")

# # print(int("23"))
# # if 3**2+4**2 == 5**2:
# #     print("345")
# # elif 3**2 <4**2:
# #     print("34")
# # else:
# #     print("5")
# # comparing string
# # if "toast" < "jam":print("toast")
# # else: print("jam")

# # if "12"<"15": print("12")
# # else: print("5")

# # a = 12.3
# # b= 100
# # c=0
# # if a < b: a = a+1; b=b-1; c=c-b
# # print(a)
# # print(c)

# # a=100
# # b=200
# # c=300
# # ab= a<b
# # cd= (c == a+b)
# # if ab and cd: print("AB and CD")
# # elif ab: print("AB")
# # else: print("Nope")

# #A program that read temperature in Celsius and convert to Fahrenheit
# # print("Enter the celsius temperatur:")
# # C = float(input()) # enter the temperature in celsius
# # F = C*9/5 + 32
# # print(f"The Fahrenheit equivalent of the celsius temperature is: {F}")
# # a= 0
# # b =0
# # while a < 10:
# #     a += 1
# # print(a)
# # count = 1
# # n = 1
# # a = 4
# # while count < 16:
# #     b = a/n
# #     count+=1
# #     n+=2
# #     print(b)

# """A progrm that determine if a number is a prime number"""

# import random
# # import math

# k = random.randint(10000, 1000000)
# # print(f"Is {k} a prime number or not? Type True or False:")
# # answer = input().strip().lower()

# # # normalize user answer to boolean
# # user_thinks_prime = answer in ("true", "t", "yes", "y", "1")

# # correct=0
# # isprime = True
# # if k < 2:
# #     isprime = False
# # else:
# #     for n in range(2, int(math.sqrt(k)) + 1):
# #         if k % n == 0:
# #             isprime = False
# #             correct+=1
# #             break

# # if user_thinks_prime == isprime:
# #     print("You are correct")
# # else:
# #     print("Not correct")
# # print(correct)

# # count=0
# # for n in range(1,int(k/2)):
# #     if k%n ==0:
# #         count+=1
# # maxv=1
# # maxcount=0
# # for k in range(1,1000):
# #     for n in range(2,int(k/2)):
# #         if k%n == 0:
# #             count+=1
# #         if count>maxcount:
# #             maxcount=count
# #             maxv= k
# # print(f"themost divisors is {maxv}, with {maxcount}")


# """Histogram with a # sign"""
# # print()
# # Q1=190000
# # Q2=340000
# # Q3=87300
# # Q4=439833
# # print("Q1:", end="")
# # for e in range(0,int(Q1/20000)):
# #     print("#", end='')
# # print(Q1)
# # print("Q2", end="")  
# # for e in range(0,int(Q2/20000)):
# #     print("#",end="")
# # print(Q2)
# # print("Q3", end="")
# # for e in range(0,int(Q3/20000)):
# #     print("#",end="")
# # print(Q3)
# # print("Q4",end="")
# # for e in range(0,int(Q4/2000)):
# #     print("#",end="")
# # print(Q4)

# # min = 24
# # min-=4
# # min+=1.1
# # print(min)
# """try while loop"""
# # i =0
# # while i < 10:
# #     sum = i*2
# #     i+=1
# # print(sum, i)

# """Error checking and validity in number choosing game"""
# # choose = 7 #computer guess
# # guess=False
# # while not guess:
# #     print("Please enter the guess number between 1 and 10")

# #     try:
# #         playerchoice = int(input()) # prompt from user
# #         guess=True
# #     except:
# #         print("Error: enter an integer")

# #         #if guess is out of range
# #     if playerchoice < 1 or playerchoice>10: 
# #         print("Your guess is out of range")
# #         guess=False

# # if choose==playerchoice:
# #     print("You winn")
# # else:
# #     print(" Sorry, You loss")
# """Add 1/2, 1/4, 1/8 up to the 20th term with the formula 1/(2**n)"""
# # total = 0
# # for term in range(1, 21):
# #     total += 1 / (2 ** term)

# # print(total)

# """Add 2/4, 2/16,2/64  up to the 10th term to add a number in sequence, first find the logical formula first"""
# # total=0
# # for n in range(2,32,2):
# #     total+=2/(2**n)
# # print(total)

# # def Newton(f,dfdx,guess,max_iter=20, tol=1e-3):
# #     f0=f(guess)
# #     iter=0
# #     while abs(f0)>tol and iter < max_iter:
# #         x1=guess-f0/dfdx(guess)
# #         guess=x1
# #         f0=f(guess)
# #         iter+=1
# #         converge=iter<max_iter
# #         return converge,iter,

# # a="elolo"
# # b=a.capitalize()
# # c=a.upper()
# # d=a.splitlines()
# # print(b, c, d)
# """using exec to print program in a doctrings"""
# # program="""list=[1,2,4,7,12,15,21]
# # for i in list:
# #     print(i, i*2)"""
# # exec (program)

# """Protons and neutrons of an atom"""

# # atoms=("Hydrogen",1,"helum",2,"LIthium",3,"Beryllium",4,"Boron",5,"Carbon",6)
# # for i in range(0,len(atoms)):
# #     if i%2==1:
# #         j=atoms[i]*2
# #         print(f"has {atoms[i]} protons and, {j}, neutrons")
# #     else:
# #         print(f"Element {atoms[i]}")

# """intersection of two set"""
# # c=0
# # a=[1,2,3,4,5,6]
# # b=[2,4,6,8,10,12]
# # for i in a:
# #     if i in b:
# #         c+=i
# #     print(c)

# """What even num less than or equal to 100 are also perfect squares"""
# import math
# A=() # list of num that are both even and perfect square
# for i in range(1,51):
#     A+=(i*2,)
# print(A)

# print()

# perfect_square=[i for i in A if (math.sqrt(i)==math.floor(math.sqrt(i)))]
# print(f"The perfect sqaure number that are even in the ramge of 1 to 100 are; {perfect_square}")
# i=3
# j=5
# # sum=0
# # if (i<4) and (j<=5):
# #     sum=sum+i+j 
# #     print(sum)
import os
print(os.getcwd())

import os 
os.makedirs("College/Python/Programs")
print(os.listdir())