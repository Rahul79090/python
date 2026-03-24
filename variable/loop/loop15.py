# # i = 1
# # while i <=10:
# #     if(i ==3):
# #         i +=1
# #         continue
# #     print(i)
# #     i +=1

# for i in range(10 , 0 , -1):
#     print("*" *i)


    
# for i in range(10 , 0 , -2):
#     print("*" *i)

# for i in range(4 , 0, -1):
#     print("*" *i)

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)