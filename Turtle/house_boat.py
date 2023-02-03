# Turtle self-assessment problems
# lets try to draw :)

import turtle
turtle.color("red")
turtle.penup()
turtle.backward(300)
turtle.pendown()
turtle.speed("slow")


def triangle(size):
    for j in range(3):
        turtle.forward(size)
        turtle.left(120)

def rectangle(short,long):
    for i in range(2):
        turtle.forward(short)
        turtle.right(90)
        turtle.forward(long)
        turtle.right(90)

def move(len):
  turtle.penup()
  turtle.forward(len)
  turtle.right(90)
  turtle.forward(len/15)
  turtle.left(90)
  turtle.pendown()

def move2(a):
  turtle.penup()
  turtle.right(90)
  turtle.forward(a)
  turtle.left(90)
  turtle.backward(a)
  turtle.pendown()

def houseboat(size):
    triangle(size)
    rectangle(size,size)
    move2(size)
    rectangle(size*3,size/2)

def main():
    houseboat(100)
    turtle.color("green")
    move(100*4)
    houseboat(75)
    turtle.color("purple")
    move(100*3)
    houseboat(25)
main()

turtle.Screen().exitonclick()