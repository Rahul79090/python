# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)


# even number ke liye 
# i = 1
# while i<=10:
#     if(i%2 !=0):
#         i +=1
#         continue #skip
#     print(i)
#     i +=1


    # odd number ke liye odd hi ki nahi
# i = 1
# while i<=10:
#     if(i%2 ==0):
#         i +=1
#         continue #skip
#     print(i)
#     i +=1


# my_set = {10 , 20, 30, 40, 50}

# sorted_list = sorted(my_set)

# mid_index = len(sorted_list) // 2

# print(sorted_list[mid_index])


# Q.8 Implement a scenario where multiple virtual machines share the same physical server (multitenancy). Show how isolation is maintained and performance metrics are monitored.

# for i in range(4 , 0, -1):
#     print("*" *i)

# Even Odd Program

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")