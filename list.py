list_1 = [1, 2, 3, 5, 9]
list_2 = [4, 5, 1, 7, 8]
list_3=[]
for i in list_1:
    if i  not in list_2:
        list_3.append(i)
print(list_3)
