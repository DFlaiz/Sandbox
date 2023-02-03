print("Hello, World")
print("Challenge #", 2+3)

import turtle

turtle.color("blue")

turtle.forward(50)
for hi in range(5):
    print(hi)

print("-"*10)

for lo in range(7,-7,-3):
    print(lo)

print("-"*10)

phrase = "Monty Python"
for letter in phrase:
  print(letter, end="-")
print()

print("END")

import turtle

turtle.color("red")

size = 100
turn = 120

for c in range(3):
    turtle.forward(size)
    turtle.right(turn)

import turtle
turtle.color("red")

#length of line
size = 100
#the angle of the turn
turn = 120
#number of turns
turns = 3

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.right(120)
import turtle

colors = ['red', 'purple', 'blue', 'orange', 'yellow']
t = turtle.pen()
turtle.bgcolor('black')
turtle.bg

for x in range(360):
  t.pencolor(colors[x%6])
  t.width(x/100+1)
  t.forward(x)
  t.left(59)