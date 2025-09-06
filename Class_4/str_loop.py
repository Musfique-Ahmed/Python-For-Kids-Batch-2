# name = "Tahmid"

# for i in name:
#     print(i, end="-")



word = "hello"
for letter in word:
    print(letter)

word = "education"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count += 1 # count = count + 1

print("Number of vowels:", count)


word = "hello"

for letter in word:
    print(letter)