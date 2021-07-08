"""Turtle drawing of a topdown pyramid."""

from turtle import *

screen = Screen()
screen.screensize(1128, 191, "black") # LinkedIn banner image size
# screen.tracer(0)

turtle = Turtle()
turtle.pencolor("white")
turtle.ht()
turtle.speed(0)

def fractal(width: int, angle:int) -> None:
    if width <= 1:
       return

    else:
        draw_square(width)

        if width % 2 == 0:
            angle *= width
        else:
            angle /= width
        width -= 1
        fractal(width, angle)

def draw_square(width):
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(width)
    

fractal(100, 20)
done()