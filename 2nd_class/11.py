# for i in range(5):
#     print("hello " + str(i))
#
# for i in range(10):
#     print(" your number is " + str(i))


def my_printer(prefix, amount_of_times):
    for i in range(amount_of_times):
        print(prefix + str(i))

def mul_five(my_number):
    result = my_number*5
    return result


the_result = mul_five(5)
print(the_result)
h = "good"
print(f"your result is {the_result} and {h}")
my_printer("hello ", 5)
my_printer("you are number ", 10)
