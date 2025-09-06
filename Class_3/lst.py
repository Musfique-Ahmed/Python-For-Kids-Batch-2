items = ["ata", "moyda", "shuji", "chini"]

print(items)

movies=["harry potter","suzume","IT"]
print(movies)

favorite_movies = [
    "The Shawshank Redemption",
    "Inception",
    "The Lord of the Rings: The Return of the King",
    "Spirited Away",
    "The Dark Knight"
]
print("My Five Favorite Movies:")
for movie in favorite_movies:
    print(f"- {movie}")


items = ["ata", "moyda", "shuji", "chini"]

print(items)

items[1] = "dim"
items[3] = "lobon"

print(items)

fruites = ["apple", "banana", "mango", "pinapple", "grape"]

if "grape" in fruites:
    print(f"grape is in the list")
else: print(f'grape is not in the list')

if "pinapple" not in fruites:
    print(f"pinapple is not in the list")





favorite_movies = [
    "The Shawshank Redemption",
    "Inception",
    "The Lord of the Rings: The Return of the King",
    "Spirited Away",
    "The Dark Knight"
]

print(favorite_movies[-4])


color=["black","mint","dark blue", "dark red"]
print(color[0])
print(color[3])
print(color[-2])



names = ["anik", "musfique", "ahmed"]

print(names[0])
print(names[1])
print(names[2])

print(f"hello {names[0]}  how are you?")
print(f"hello {names[1]}  how are you?")
print(f"hello {names[2]}  how are you?")



classes = []

classes.append("tasnia")
print(classes)

classes.append("Nusaybah")
print(classes)

classes.insert(0, "musfique")
print(classes)

classes.append("anik")
print(classes)


names=[]
names.append("Akito")
names.append("Yuji")
names.append("remi")
names.insert(1,"Raven")
print(names)

names.pop()
print(names)



fruites = ["apple", "banana", "mango", "pinapple", "grape"]

fruites.remove("banana")
print(fruites)

del fruites[0]
print(fruites)

removed_item = fruites.pop()
print(removed_item)
print(fruites)

removed_item = fruites.pop(0)
print(removed_item)
print(fruites)



food=["orange","lemon","apple","banana"]
food.remove("orange")
print(food)
food.pop(2)
print(food)

fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.remove("Mango")
print("Updated fruits list:", fruits)
fruits.pop(2)
print(fruits)


fruites = ["apple", "banana", "mango", "pinapple", "grape"]

print(fruites[1:4])
print(fruites[ :3])
print(fruites[2: ])



num = [10, 20, 30, 40, 50]
first_three = num[:3]
print("First three numbers:", first_three)
items = ['apple', 'banana', 'carrot', 'grapes', 'egg']
middle = items[2:3]
print("Middle item:", middle)
middle_three = items[1:4]
print("Middle three items:", middle_three)


numbers = [12,34,56,78,23]
fruits=["apple","banana", "mango","pinapple","grape"]
first_item = numbers[:3]
print("First item (as a list):", first_item)
print("First item (as a number):", numbers[0])
items = ["A", "B", "C", "D", "E"]
middle_three = items[1:4]
print("Middle three items:", middle_three)





fruits=["apple","banana", "mango","pinapple","grape"]

copy_fruits = fruits.copy()

print(copy_fruits)

copy_fruits.pop()

print(copy_fruits)

print("Real", fruits)


numbers = [12,34,56,78,23, 9]
numbers.sort()
print(numbers)

numbers.reverse()

print(numbers)


print(len(numbers))


number = (10,20,30)
print(number)
# number[0] = 40
# number.append(60)