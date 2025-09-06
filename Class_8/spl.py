txt = "Hi, there, my name is anik"

lst = txt.split()

print(lst)


lst_2  = txt.split(',')
print(lst_2)


f_name, l_name = input("Enter you name: ").split()
# print(f_name, l_name) name, age , gender
print(f"First name: {f_name} \nLast name: {l_name}")


lst = input("Enter you fav fruits: (Give coma between them!)").split(',')
print(lst)

f_name, l_name, age, gender = input("Enter you name, age, gender (Give spaces in between): ").split()
print(f"First name: {f_name} \nLast name: {l_name} \nAge: {age} \nGender: {gender}")


