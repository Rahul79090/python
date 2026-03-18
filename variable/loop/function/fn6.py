# #wap to print the element of a list in a single line.(list is the parameter)

# cities = ("delhi","gurgaon","noida","pune","mumbai","chennai")
# heroes = ["thor", "ironman","captain america","shaktiman"]

# # print(cities[1], end= "\n")
# # print(cities[3], end= "\n")
# def print_len(list):
#     print(len(list))

#     # print_len(cities)

# def print_list(list):
#     for item in list:
#         print(item, end = " ")

# print_list(heroes)
# print()


#wap to find the factorial of n
# n= 5
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *=i

#     print(fact)
# cal_fact(5)

# wap to convert usd to INR

# def converter(usd_val):
#     inr_val = usd_val*83
#     print(usd_val,"usd =",inr_val, "INR")

# converter(100)


# add even in function

def check_add_even(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")

        # function call
check_add_even(10)
check_add_even(7)
