# reading exercise
# By Doris Flaiz

# DoW = input("What day is it? ")
#
# if DoW.capitalize() == "Saturday":
#     print("Wake up at 9 am")
# elif DoW.capitalize() == "Sunday":
#     print("Wake up at 10 am")
# else:
#     print("Wake up at 7 am")

temp = eval(input("What's the temperature outside? "))

if temp > 90:
    print("Whoa, it's boiling!")
elif temp >= 80:
    print("It's getting hot")
elif temp >= 60:
    print("A perfect day")
elif temp >= 32:
    print(("Don't forget your sweater"))
else:
    print("Brrr, you need a coat")

wear = input("What's shuld you be wearing? ")