#Q1
# a
# saying = "howdy"
# for u in saying.upper():
#     print(saying, end= "!! ")
# print()

# b
# t = 20
# for v in range(2, 12,3):
#     t += v
# print(t)

# 20+2
# 22+5
# 27+8
# 35+11
#
# t=46
#
# for i in range(5,26,5):
#     print(i)
#
# for j in range(5,9):
#     print(j, end="... ")
# print("who do we appreciate?")
#
# for char in "GOODBY":
#     print(char, end="-")
# print("E!")

# example from previous quiz
# sum = 0
# for i in range(5):
#     sum += eval(input("Please enter a grade: "))
# avg = sum / 5
# print("Current average:", avg)
#print("25% improvement:", 1.25 * avg)
#
# for team in range(3):
#     t = input("Please enter a team name: ")
#     print("Go...", t.upper()+"!")
#     print()

# example from previous quiz
# for i in range(-1, 5):
#     print(int(4 ** i), end=' ')

# Q5
# have the user input numbers and capture in a list
enternum = 5
numlist = []
for i in range(enternum):
    numlist.append(eval(input("Please enter a number: ")))
# print(numlist)

# take that list and get the square of each number entered
result = [number ** 2 for number in numlist]
# print(result)

# add all the squared numbers together
sum = 0
for n in result:
    sum += n
# print("squared added together", sum)
print("the average of each number squared", sum / enternum)
