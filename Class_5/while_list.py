registered = ["Anik", "Musfique", "Ahmed", "Anik"]

verified = []

while registered:
    temp = registered.pop()
    verified.append(temp)

print(registered, verified)


registered = ["Anik", "Musfique", "Ahmed", "Anik", "Anik", "Anik", "Anik"]

while "Anik" in registered:
    registered.remove("Anik")
print(registered)