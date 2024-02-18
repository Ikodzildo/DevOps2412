# A.
# print(f"Input a number")
# x = int(input())
# print(f"Input a number")
# y = int(input())
#
# if type(x) is int:
#     if int(x) > int(y): print("BIG")
#     elif x < y: print("small")
#     else: print("Numbers are equal")
# else:
#     print("either x or y or both are not integers")


# B.
#
# for i in range(5):
#     print(i)


# C.

# var = x = int(input("choose a number between 1-4"))
#
# if var == 1:
#     print("1 = Summer")
# elif var == 2:
#     print("2 = Winter")
# elif var == 3:
#     print("3 = Fall")
# elif var == 4:
#     print("4 = Spring")
# else:
#     print("Number is not 1-4")

# D.
# loop will run 10 times
# number 10 will be printed last



# E.
# age = 45
# lastname = "k"
# shekel_dollar_rate = 0.27
# fly_aborad = True
# app_num = 1
# print(f"My Ageis : {age}\nMy Last Name is: {lastname}\nShekel-Dollar Rate is: {shekel_dollar_rate}\nFlew abroad: {fly_aborad}\nApparetment number: {app_num}")
# print(age+shekel_dollar_rate)


# F.
# phone = input("please provide your 10 digit phone number: ")
# if len(phone) == 10:
#     print(f"phone number: {phone}")
# else:
#     print("please provide your 10 digit phone number again: ")
#


# G.
# def printHello():
#     print("hello")
#
# def calculate():
#     print(5+3.2)
#
# printHello()
#
# calculate()
#

# H.

# def getname():
#     getname = input("please add you name:")
#     print(f"Your name is: {getname}")
# def divide(number):
#     print(number/2)
#
# getname()
# divide(5)


# I.
# def adder(num1, num2):
#     return num1 + num2
#
#
# def add_space_between_strings(str1, str2):
#     return str1+" "+str2
#
#
# result = adder(5, 2)
# print(f"Result is: {result}")
#
# print(add_space_between_strings("ido", "kodzidlo"))


#challenges
# K.
# print("set a number: ")
# getnumber = int(input())
#
# for i in range(1, getnumber + 1):
#         print("#" * (i))


#L.
# print("set a number: ")
# getnumber = int(input())
# for i in range(getnumber):
#         for j in range(getnumber):
#             if i == j or i + j == getnumber - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#
#         print()

#M.
# class t:
#     def getnumber(self):
#         print("set a 2 digit number: ")
#         getnumber = input()
#         self.sum(getnumber)
#
#
#     def sum(self,getnumber):
#         y = int(getnumber[0])
#         x = int(getnumber[1])
#         print(x+y)
#
# myinstance = t()
# myinstance.getnumber()