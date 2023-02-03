# Turtle self-assessment problems
# lets try to draw :)

import turtle
turtle.speed("fast")
turtle.color("red")
turtle.penup()
turtle.backward(300)
turtle.pendown()

def rectangle(short,long):
    for i in range(2):
        turtle.forward(short)
        turtle.right(90)
        turtle.forward(long)
        turtle.right(90)

def octagon(size):
    for k in range(8):
        turtle.forward(size)
        turtle.left(45)

def move(len):
  turtle.penup()
  turtle.forward(len)
  turtle.pendown()

def sign(size):
    octagon(size)
    move(size*3/8)
    rectangle(size/5,size*2)

def main():
    sign(25)
    turtle.color("blue")
    move(100)
    sign(50)
    turtle.color("purple")
    move(200)
    sign(75)

main()

turtle.Screen().exitonclick()