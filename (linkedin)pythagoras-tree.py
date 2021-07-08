"""Turtle drawing of my own pythagoras tree variation. https://en.wikipedia.org/wiki/Pythagoras_tree_(fractal)."""
from turtle import *
import math

ANGLE_1 = 40
ANGLE_2 = 130
SCALE_FACTOR = (math.sqrt(2) / 2)

screen = Screen()
screen.screensize(1584, 396, "black") 
screen.tracer(0)

turtle = Turtle()
turtle.pencolor("white")
turtle.ht()
turtle.speed(0)

def fractal(width: int, angle:int, start_pos, end_pos) -> None:
    if width <= 4:
       return

    else:
        draw_square(width)
        top_left_pos = turtle.pos()
        heading = turtle.heading()
        turtle.left(ANGLE_1)
        fractal(SCALE_FACTOR * width, angle, 0, 0)

        turtle.goto(top_left_pos)
        turtle.seth(heading)
        turtle.fd(width)
        turtle.left(ANGLE_2)
        fractal(SCALE_FACTOR * width, angle, 0, 0)

def draw_square(width):
    for count in range(3):
        turtle.fd(width)
        turtle.left(90)
    turtle.fd(width)
    turtle.bk(width)
    turtle.left(90)
    

fractal(1000, 20, 0, 0)
screen.getcanvas().postscript(file="duck.eps")
done()

