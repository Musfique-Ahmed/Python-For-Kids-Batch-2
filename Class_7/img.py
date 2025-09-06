with open("test.jpg", 'rb') as file:
    content = file.read()

# print(content)

with open('test_2.png', 'wb') as file:
    file.write(content)