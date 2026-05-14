# name ="rahul kuamr"
# age = 19
# price = 25.6
# print("my name is :-", name)
# print("my age is :-",age)
# print("my price is :-",price )

# print(type(name))
# print(type(age))
# print(type(price))

# name1 = "rkg"
# name2 = 'rkg'
# name3 = '''rkg'''

# print(name1)
# print(name2)
# print(name3)


# age =23
# old = False
# a = None
# print(type(old))
# print(type(a))



# arr = [5, 2, 9, 1, 7]

# max_val = arr[0]

# for num in arr:
#     if num > max_val:
#         max_val = num

# print("Maximum =", max_val)


# Complex Array Operations in Python using NumPy

import numpy as np

# Create a complex array
arr = np.array([2+3j, 4+5j, 6+7j])

print("Complex Array:")
print(arr)

# Real part
print("\nReal Parts:")
print(arr.real)

# Imaginary part
print("\nImaginary Parts:")
print(arr.imag)

# Conjugate of complex numbers
print("\nConjugate:")
print(np.conj(arr))

# Magnitude (absolute value)
print("\nMagnitude:")
print(np.abs(arr))