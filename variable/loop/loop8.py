# print(range(5))

# seq = range(10)

# for i in seq:
#     print(i)

# for i in range(2, 10): #range(start , stop)

#     print(i)


# for i in range(2, 10 ,2): #range(start , stop , step)
    
#     print(i)

# for i in range (2 , 101, 2):
#     print(i)

# for i in range (2 , 101, 2):
#     print(i)

nums = (1 , 4, 9, 16, 25, 49, 64, 81, 100,49)

x =49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx",idx)
    idx += 1
