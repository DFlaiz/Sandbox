# Activity - Using Functions - Quiz

#Asking user for their favorite month and day

import math

name = input("Please enter your name: ")
num = input("Now please enter your favorite number: ")

print("Your favorite number is: ", name.capitalize()+"\'s Number")

print("Is the number decimal? ", num.isdecimal())
print("The number of 1's in your favorite number: ", num.count("1"))
print("The factorial of the number: ", math.factorial(int(num)))
print("The Log Base 5 of the number: ", math.log(float(num), 5))