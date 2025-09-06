my_dict={"first name":"kazi",
         "last name":"tasnia",
         "age":15,
         "dob":"26/04/2010"}


for key in my_dict.keys():
    print(key)


for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key} : {value}")



students_marks={"Nusaybah":"19",
                "ahnaf":"18",
                "Eilma":"16"}
for key,value in students_marks.items():
    print(f"{key} : {value}")