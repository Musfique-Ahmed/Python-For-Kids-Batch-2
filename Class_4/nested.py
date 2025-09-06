# matrix = [[1,2], [3,4], [5,6]]

# for row in matrix:
#     for i in row:
#         print(i, end=" ")

#     print()


for i in range(1,6):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    
    print("-----***-----")


for i in range(10):
    for j in range(10):
        print("*", end="")
    print()