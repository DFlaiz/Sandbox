# Activity - Using Functions - Quiz

#Asking user for their favorite month and day

import math

month = input("Please enter your favorite month: ")
day = input("Now please enter your favorite day: ")

print("You entered: ", month.capitalize(), day + "," , "2020")

print("Is the month alphanumeric? ", month.isalnum())
print("The number of 2's in the day: ", day.count("2"))
print("The factorial of the day: ", math.factorial(int(day)))
print("The Log Base 2 of the day: ", math.log2(int(day)))