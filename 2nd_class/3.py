a = 5
b = 14
my_name = "Ido"
if a < 10:
    print("you are Ido Kodzidlo")
    print("Hello")
    print("World")
elif my_name == "Ido":
    print("found your name")
elif b > 5:
    print("b is good")
else:
    print("blabla")

print (a==50)
should_i_work_today = a == 50 and b < 100
if should_i_work_today:
    print("go to work")
else:
    print("stay at home")

my_list = []
if my_list:
    print("you have item")
else:
    print("you have no item")

my_other_list = ["or", "tohar", "ido"]
my_other_name = "moshe"
if my_other_name in my_other_list:
    print("I found moshe")
else:
    print("moshe not found")

tt= [1,2,3]
rr= [1,2,3]
print(type(tt) is list)
