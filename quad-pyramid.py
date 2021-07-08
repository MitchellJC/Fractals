"""Turtle drawing of a quad pyramid"""

from turtle import *

screen = Screen()
screen.screensize(1128, 191, "black") # LinkedIn banner image size
# screen.tracer(0)

turtle = Turtle()
turtle.pencolor("white")
turtle.ht()
turtle.speed(0)

def fractal(width: int, angle:int, start_pos, end_pos) -> None:
    if width <= 1:
       return

    else:
        draw_square(width)
        width -= 1
        fractal(width, angle, 0, 0)

def draw_square(width):
    for count in range(3):
        turtle.fd(width)
        turtle.left(90)
    turtle.fd(width)
    turtle.bk(width)
    turtle.right(180)
    

fractal(100, 20, 0, 0)
done()