# Have user enter a decimal as input and perform various actions on that number
import math

num = eval(input("Please enter a decimal number: "))
# print(type(num)) #verifying that my entry is not a string

print("The Absolute Num", abs(num))
print("The Rounded Num", round(num,0))
print("The SQRT of the Absolute of the Rounded Num", math.sqrt(abs(round(num, 0))))