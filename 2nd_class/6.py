for i in range(5):
    print("hello " + str(i))
else:
    print("finished")

class_mates = ["maksim", "yoni", "gilad", "oren"]
for name in class_mates:
    if name == "yoni":
        name = "amir"
    print(name)

for i in range(len(class_mates)):
    print(class_mates[i])

your_name = input("enter your name: ")
while your_name != "ido":
    print("you are not ido")
    if your_name.lower() =="haim".lower():
        print("oh my god")
        break
    if your_name == "david":
        print("wow!")
        continue
    your_name = input("enter your name: ")
else:
    print("your name is ido")