a = range(1, 101, 1)

for num in a:
    if num % 7 != 0 and '7' not in str(num):
        print(num)
    else:
        print("Boom")
