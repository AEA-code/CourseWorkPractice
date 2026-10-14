# #converting binary, hexadecimal, octal to decimal and vice versa
# print("binary convertion")
# print(int("101",2))
# print(bin(5))
# print("Hexadecimal convertion")
# print(int("ADF", 16))
# print(hex(15))
# print("Octal convertion")
# print(int("234", 8))
# print(oct(3))
# print()
# a = True
# b  = False
# print(a and b)
# print(a or b)
# print(not a)
# print(a !=b) # XOR
# print()
# #computing logic gate
# x= 0b1010
# y= 0b1100
# print(bin(x & y))# AND GATE
# print(bin(x | y))#OR GATE
# print(bin(x ^ y)) #XOR
# print(bin(~ x & 0b1111))
# print()
#print truth table
# for a in [0, 1]:
#     for b in [0, 1]:
#         print(b)
#         print()
#         print(a)#, a and b, a or b, a !=b)
#         print()
#         print(a and b)
#         print()
#         print(a or b)
#         print(a != b)
# converting decimal 14 to bin, oct and hex
# a = 14
# print(a)
# b = bin(a)
# print(b)
# c = oct(a)
# print(c)
# d = hex(a)
# print(d)

"""A function that perform binary addition of two imput"""
def add_binary():
   #make length equal by padding with
    A = input('enter the first binary number: ')
    B = input('enter the second binary number: ')

    max_len = max(len(A),len(B))
    A = A.zfill(max_len)
    B = B.zfill(max_len)

    carry = 0
    result = []

    #start from rightmost bit
    for i in range(max_len -1,-1,-1):
        bit_A = int(A[i])
        bit_B = int(B[i])

        total = bit_A + bit_B + carry

        result_bit = total % 2
        carry = total // 2

        result.append(str(result_bit))

    # if carry remains
        if carry:
            result.append(str(carry))

        #Reverse result because I built it backwards
        result.reverse()

        return "".join(result)
z = add_binary()
print(z)