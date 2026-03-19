
# n = int(input("enter the value of n:-"))
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1) 
#     print("end")

# show(n)

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n* fact(n-1)

# print(fact(5))

# write a recursive function to calculate the sum of first n natural numbers.

# n = int(input("enter the value of n:-"))
# def calc_sum(n):
#     if(n ==0):
#         return 0
#     # print(n)
#     return calc_sum(n-1)+n

# sum = calc_sum(n)
# print(sum)

n = int(input("enter the value of n:-"))
def calc_sum(n):
    if(n ==0):
        return 0
    # print(n)
    return calc_sum(n-1)+n

sum = calc_sum(n)
print(sum)
