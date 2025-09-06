lst = [1,2,3,4,5]

for i in lst:
    print(i)


for i in range(1,11,2):
    print(i)


st = (2,3,4,5)

dic = {
    'Name': "anik",
    'Age': 23,
    "gender": 'Male'
}

print(dic.keys())

for key in dic.keys():
    print(key)


for value in dic.values():
    print(value)

for key, value in dic.items():
    print(f"{key}  :  {value}")


x = 0
while x<100:
    print(x)
    x += 1 #increment


# while True:
#     print('How are you?')


user_input = input("Tell about yourself!(Enter quit to close): ")
while user_input.lower() != "quit":
    user_input = input("Tell about yourself!(Enter quit to close): ")