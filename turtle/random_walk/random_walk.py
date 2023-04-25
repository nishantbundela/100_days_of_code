import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fast")

for i in range(200):
    tim.forward(40)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colours))