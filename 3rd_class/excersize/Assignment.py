#1

# a = 1 / 0

#2
# try:
#     a=1/0
# except ZeroDivisionError:
#     print("could not divide by zero")

#3
# try:
#     x=1
# finally:
#     print("finally")

#4
# Any exception type

#5
# it will give only partial exception information

#6
#it can handle input output errors and zero division error

#7 - 9
# def add_words():
#     a = open("words.txt", "a", encoding="utf-8")
#     word = input("Add a word:")
#     a.write(word + "\n")
#     a.close()
#
# def read_file():
#     my_file = open("words.txt", "r", encoding="utf-8")
#     for name in my_file.readlines():
#         print(f"hello {name}", end='')
#     my_file.close()
#
# read_file()
# add_words()

#challenge

#11
# imports Pil module
# from PIL import Image
#
# # creating image object which is of specific color
# im = Image.new(mode="RGB", size=(200, 200),
#                    color=(153, 153, 255))
#
# # this will show image in any image viewer
# im.show()