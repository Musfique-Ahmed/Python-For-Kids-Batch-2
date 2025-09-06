family = {
    "Child1": {
        "Name": "Anik",
        "Age": 21,
        "DOB": "07/05/2004"
    },
    "Child2":{
        "Name": "Musfique",
        "Age": 22,
        "DOB": "05/07/2004"
    }
}

# Main Dictionary
print(family)

# key of the Main Dictionary
print(family["Child1"])

# value of the nested dictionary
print(family["Child1"]["Name"])




class1 = {
    "stu1": {
        "Name": "Anik",
        "Age": 21,
        "DOB": "07/05/2004",
        "Marks": 23
    },
    "stu2":{
        "Name": "Musfique",
        "Age": 22,
        "DOB": "05/07/2004",
        "Marks": 24
    }
}


print(class1["stu1"]["Marks"])


# List inside dict

subs = {
    "stu1":["Bangla", "eng"],
    "stu2":["math", "science"]
}

print(subs["stu1"][0])