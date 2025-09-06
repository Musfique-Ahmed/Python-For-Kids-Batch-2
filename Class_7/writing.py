# with open("random_2.txt", "w") as file:
#     file.write("UOops! I just deleted the info!")
#     print("File handling Done!")


# with open('random.txt', 'a') as file:
#     file.write("\n UOops! I just deleted the info!")
#     print("File handling Done!")


lines = ["Hello" ,"This is a test", "Python is fun", "End of file"]
with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

print("appending this line.")