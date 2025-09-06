my_dict = {"First name": "Musfique",
           "Last name": "Ahmed",
           "Age": 21,
           "DOB": "07/05/2004"
           }

print(my_dict)

my_dict={"first name":"kazi",
         "last name":"tasnia",
         "age":15,
         "dob":"26/04/2010"}

print(my_dict)

my_dict={"first name":"Nusaybah",
        "last name":"Bint Mezbah",
        "age":"12"}
print(my_dict)


print(my_dict["age"])

my_dict["age"] = 13

print(my_dict["age"])
print(my_dict)

del my_dict["age"]

print(my_dict)

my_dict.pop("last name")
print(my_dict)




my_dict = {"First name": "Musfique",
           "Last name": "Ahmed",
           "Age": 21,
           "DOB": "07/05/2004"
           }

# uodate key
my_dict["Age"] = 22

# add key
my_dict["University"] = "UIU"

# delete key
del my_dict["DOB"]

print(my_dict)


my_dict["age"]=13
my_dict["school"]= "Primier School Dhaka"
# del my_dict["DOB"]



my_dict={"first name":"kazi",
         "last name":"tasnia",
         "age":15,
         "dob":"26/04/2010"}

my_dict["age"]=15
my_dict["school"]="mubc"
del my_dict["dob"]
print(my_dict)


fav_book = {
    "The Productive Muslims": "MD. Faris"
}

fav_book["The Productive Muslims"] = "Md. Faris"
fav_book["Paradoxical Sajid"] = "Arif Ajad"

print(fav_book)

fav_book.clear()

print(fav_book)