import turtle as t
import random

tim = t.Turtle()

def random_color():
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fast")

for i in range(200):
    tim.forward(40)
    tim.setheading(random.choice(directions))
    tim.color(random_color())