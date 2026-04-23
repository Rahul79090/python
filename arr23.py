# arr = [5, 2, 9, 1, 7]

# max_val = arr[0]

# for num in arr:
#     if num > max_val:
#         max_val = num

# print("Maximum =", max_val)

n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Array is:", arr)