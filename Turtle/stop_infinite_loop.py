from turtle import Turtle, Screen

def draw_sunshine(turtle):
    turtle.penup()
    turtle.goto(50, 50)
    turtle.pendown()
    turtle.color('black', 'yellow')
#    turtle.speed("fast")

    turtle.begin_fill()

    for _ in range(24):
        turtle.forward(100)
        turtle.left(75)

    turtle.end_fill()

screen = Screen()
screen.setup(800, 600)

yertle = Turtle()

weather = ''

while not weather:
    weather = input("Would you like to draw 'rain' or 'sunshine'? ")

    if weather == "rain":
        draw_rain(yertle)
    else:
        draw_sunshine(yertle)

yertle.hideturtle()
screen.exitonclick()