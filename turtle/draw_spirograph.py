import turtle as t
import random

eva = t.Turtle()
eva.speed("fast")

def random_color():
    r = random.uniform(0, 1)
    g = random.uniform(0, 1)
    b = random.uniform(0, 1)
    color = (r, g, b)
    return color

for i in range(20):
    eva.circle(100)
    eva.lt(18)
    eva.color(random_color())

screen = t.Screen()
screen.exitonclick()