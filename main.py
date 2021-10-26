import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

color_list = [(152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183),
              (196, 94, 75),
              (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71),
              (232, 176, 165),
              (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85),
              (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]
t = Turtle()
t.speed("fastest")
t.penup()
t.setx(-230)
t.sety(-230)
a = -180
score = 0
runtime = True
while runtime:
    for _ in range(9):

        t.dot(20, random.choice(color_list))
        t.penup()
        t.fd(50)
        t.dot(20, random.choice(color_list))
        if _ == 8:

            t.setx(-230)
            t.sety(a)
            a += 50
            score += 1
        elif score == 9:

            runtime = False

screen = Screen()
screen.exitonclick()



