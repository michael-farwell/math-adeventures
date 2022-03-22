from turtle import *

speed('fast')


def triangle(length=100):
    """
    Draws a triangle given a side length
    """
    for i in range(3):
        forward(length)
        right(120)


def square(length=100):
    """
    Draws a square given a side length
    """
    for i in range(4):
        forward(length)
        right(90)


def polygon(sides=3, length=100):
    """
    Draws a polygon given a number of sides
    """
    angle = 360 / sides
    for i in range(sides):
        forward(length)
        right(angle)


def circle_squares(length=100):
    """
    Draws a circle of squares
    """
    for i in range(60):
        square(length)
        right(5)


def spiral(start_length=5):
    for i in range(60):
        square(start_length + (5 * i))
        right(5)


def star(length=100):
    """
    Draws a 5-pointed star
    """
    for i in range(5):
        forward(length)
        right(144)


def star_spiral(start_length=5):
    for i in range(60):
        star(start_length + (5 * i))
        right(5)


star_spiral()

Screen().exitonclick()
