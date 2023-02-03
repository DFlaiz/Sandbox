#SA for defining more functions
#By Doris Flaiz

#What is output by the following python program?
# I came up with 8

def f(x):
    y = -4
    for z in range(x):
        y += z
    return x * y

print(f(4))

#What is output by the following python program?
# I came up with "aaaargh' forgot the !

def argh(num):
    yell = ""
    for i in range(num):
        yell += "a"
    return yell + "rgh!"

print(argh(4))

#Assume the following function is defined:
# I came up with 1. True and 2. False

def is_multiple(num, mult):
    return num % mult == 0
#What is returned by the function calls below?
print(is_multiple(25, 5))
print(is_multiple(6, 4))

#Assume the following function is defined:
# I came up with 1. 23 and 2. 20

def fun(x, y, z):
    return x * y + z

#What is returned by the function calls below?
print(fun(3, 5, 8))
print(fun(4, 2, 12))

#5

# write function for pyramid
# by Doris

def square(width):
    for i in range(width):
        print('+' * width)

square(4)

def squared(n):
    return n * n

print(squared(4))

def horiz_bar(line,width):
	for i in range(1):
		print("+" + "-" * (line -2) + "+")

def space_bar(line,width):
    for i in range(1):
        print("|", " " * ((width -1) //3), end="")
        print("|", " " * ((width -1) //3), end="")
    print("|")

def window(line,width):
    horiz_bar(line,width)
    space_bar(line,width)
    horiz_bar(line,width)
    space_bar(line,width)
    horiz_bar(line,width)

window(7,5)

#8
# using 10 different colors
import turtle
turtle.penup()
turtle.backward(300)
turtle.pendown()
colors = ['red', 'purple','blue', 'green', 'orange', 'yellow', 'teal', 'magenta','black','cyan']
def rectangle(long):
    for x in range(10):
        turtle.pencolor(colors[x%10])
        turtle.width(x/10+1)
        for l in range(2):
            turtle.forward(long)
            turtle.right(90)
            turtle.forward(long//2)
            turtle.right(90)
        long += 10

rectangle(30)

turtle.Screen().exitonclick()

def f(x):
    return g(x) + 1

def g(y):
    return y * 3

def h(num):
    print("g is", g(num))
    print("f is", f(num))


h(4)




