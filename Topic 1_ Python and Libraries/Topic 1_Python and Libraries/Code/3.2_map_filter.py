numbers = [1, 2, 3, 4]
# ---- use for loop ----
# rst =[]
# for i in range(len(numbers)):
#     n = numbers[i]
#     square = n ** 2
#     rst.append(square)

# print(rst)

# ---- map -------
# numbers = [1, 2, 3, 4]

# def square_value(x):
#     return x ** 2

# square = map(square_value,numbers)
# square = list(square)

# print(square)

# ---- lambda function -------

# def square_value(x):
#     return x ** 2
# square = lambda x: x ** 2
# s = square(2)
# print(s)

# ----------- map, lambda function ------
# numbers = [1, 2, 3, 4]
# square = map(lambda x: x**2, numbers)
# square = list(square)
# print(square)

# ----------- filter -------------

# numbers = [1, -2, 3, -4]

# positive_numbers = filter(lambda x: x>0 ,numbers)
# positive_numbers = list(positive_numbers)
# print(positive_numbers)

# --------- list comprehension --
numbers = [1, 2, -3, 4]
squares = [i**2 for i in numbers if i>0 ]

print(squares)





