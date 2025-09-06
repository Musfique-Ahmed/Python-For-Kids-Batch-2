# with open('random.txt', 'r') as file:
#     content = file.read()
#     print(content)


# # Readline only captures the first line of the file!
# with open('random.txt', 'r') as file:
#     content = file.readline()
#     print(content)

# Readlines captures all the lines and put them in a list!
with open('random.txt', 'r') as file:
    content = file.readlines()
    print(content)


for i in content:
    print(i)

print(f"The number of lines in the file: {len(content)}")