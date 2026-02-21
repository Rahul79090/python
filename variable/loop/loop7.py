# tup = {1, 2, 3, 4,2,8,9}

# for num in tup:
#     print(num)

# str = "rahul kumar sahani"

# for char in str:
#     print(char)
# else:
#     print("end")

# str = "rahul kumar sahani"

# for char in str:
#     if(char =='k'):
#         print("k is found")
#         break
#     print(char)
# else:
#     print("end")

# print the element of the following list using a loop
# [1 , 4, 9, 16, 25, 49, 64, 81, 100]
# list = [1 , 4, 9, 16, 25, 49, 64, 81, 100]

# for num in list:
#     print(num)


# list = (1 , 4, 9, 16, 25, 49, 64, 81, 100,49)

# x =49
# ind = 0
# for num in list:
#     if(num == x):
#         print("element is found ",ind)
#         ind +=1
#         break
#     print(num)
# else:
#     print("not found")

nums = (1 , 4, 9, 16, 25, 49, 64, 81, 100,49)

x =49

idx = 0
for el in nums:
    if(el == x):
        print("number found at idx",idx)
    idx += 1
