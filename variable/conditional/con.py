# wap to check if a number entered by the user is odd or even
# num = int (input("enter the number :-"))

# if(num %2==0):
#     print("the number is even:-")
# else:
#     print("the number is odd")   

# wap to find the greatest of 3 numbers entered by the user.

num1 = int (input("enter the first number :-"))
num2 = int (input("enter the second number :-"))
num3 = int (input("enter the third number :-"))

if(num1 >= num2 and num1 >= num3):
    print("the greatest number is ", num1)
elif(num2 >= num1 and num2 >= num3):
    print("the greatest number is ", num2)
else:
    print("the greater number is ",num3)