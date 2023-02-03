# What is output by the following python program?
#1

# def what(num):
#     tip = -3
#     for i in range(num):
#         print(tip, 1)
#         tip += i
#         print(tip, 2)
#     return tip
#
# print(what(5))
#2
#
# def is_negative(x):
#     return x < 0
#
# is_negative(4)
# is_negative(-4)

#3
def rectangle(width, height):
   for i in range(height):
       print("*" * width)

rectangle(5,3)

# def a(x):
# 	return b(x - 1) * 2
# def b(x):
# 	return x - 4
# def c(x, y):
# 	if x % 2 == 0:
# 		return x + 3 * y
# 	else:
# 		return x - y
# print(c(5, b(8)))
# print(c(a(3), b(5)))
