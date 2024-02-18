details = ["ido", "kod", 34, True]

details_dict = {"fname": "ido",
                "lname": "kod",
                "age": 34,
                "is_married": True}
my_class = [
    {"fname": "or", "lname": "shemesh"},
    {"fname": "maksim", "lname": "hamkasim"}
]

for student in my_class:
    print(student["fname"])

print(details_dict.keys())
print(details_dict.values())
my_other_dict = {
    0: "moshe",
    1: "haim",
    2: 56,
    3: True}