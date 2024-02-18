
def add_names():
    my_file = open("names.txt", "a")

    for i in range(3):
        current_name = input("enter name:")
        my_file.write(current_name + "\n")

add_names()
def read_file():
    my_file = open("names.txt", "r")
    for name in my_file.readlines():
        print(f"hello {name}", end='')

read_file()