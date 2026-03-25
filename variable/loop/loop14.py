# find the sum of first n natural number
# n = int(input("enter the natural number"))
# sum = n*(n+1)/2
# print("sum is :-", sum)


# Find the factorial of a given number.
# n = int(input("enter the natural number"))
# sum = n*(n+1)/2
# print("sum is :-", sum)


# i = 1
# while i <=10:
#     if(i ==3):
#         i +=1
#         continue
#     print(i)
#     i +=1

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)