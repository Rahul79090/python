list = (1 , 4, 9, 16, 25, 49, 64, 81, 100,49)

x =49
ind = 0
for num in list:
    if(num == x):
        print("element is found ",ind)
        ind +=1
        break
    print(num)
else:
    print("not found")