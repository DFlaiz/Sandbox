# Turtle self-assessment problems
# lets try to draw :)

import turtle
turtle.color("red")
turtle.penup()
turtle.backward(200)
turtle.pendown()

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def triangle(size):
    for j in range(3):
        turtle.forward(size)
        turtle.left(120)

def move(len):
  turtle.penup()
  turtle.forward(len)
  turtle.pendown()

def house(len):
    square(len)
    triangle(len)


def main():
    turtle.speed(6)
    house(100)
    move(200)
    turtle.color("blue")
    house(50)
    move(150)
    turtle.color("purple")
    house(75)

main()