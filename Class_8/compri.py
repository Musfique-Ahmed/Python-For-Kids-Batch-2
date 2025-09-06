lst = [1,4,5,7,8]

lst_sq = []

for i in lst:
    print(i**2)
    lst_sq.append(i**2)



print(lst_sq)




lst_sqr = [x**2 for x in lst]
print(lst_sqr)