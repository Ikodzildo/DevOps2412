
fname = "Ido"
lname = "Kodzidlo"
age = "34"
full_name="Ido " + "Kodzidlo"
full_name= fname + " "+ lname
Another_full_name = "%s %s %s" % (fname, lname, age)
Another_full_name2 = f"{fname} {lname}"
Another_full_name3 = "{} {}".format( fname, lname)
print(full_name)
print(Another_full_name)
print(Another_full_name2)
print(Another_full_name3)
Another_full_name_description = "name: \"ido\" \nmaried: yes\nage:34"
print(Another_full_name_description)


