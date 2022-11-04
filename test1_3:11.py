"""IPRP class test 1, 2020-11-03 15:30:00 UTC"""

import turtle
import math


def draw_square(x, y, lado, t, color):
    """Draws a square with the given side length and color on x and y coordinates."""
    t.penup()
    t.home()
    t.fillcolor(color)
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.fd(lado)
        t.right(90)
    t.end_fill()


def draw_triangle(x, y, lado, t, color):
    """Draws a triangle with the given side length and color on x and y coordinates."""
    t.penup()
    t.home()
    t.fillcolor(color)
    t.goto(x, y)
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.fd(lado)
        t.left(120)
    t.end_fill()


def draw_youtube(lado_quadrado_grande, lado_quadrado_pequeno, lado_triangulo):
    """Draws the youtube logo with the given side lengths."""
    t = turtle.Turtle()
    t.ht()
    draw_square(
        -lado_quadrado_grande / 2,
        lado_quadrado_grande / 2,
        lado_quadrado_grande,
        t,
        "white",
    )
    draw_square(
        -lado_quadrado_pequeno / 2,
        lado_quadrado_pequeno / 2,
        lado_quadrado_pequeno,
        t,
        "grey",
    )
    draw_triangle(
        (-math.sqrt(math.pow(lado_triangulo, 2) - math.pow(lado_triangulo / 2, 2))) / 2,
        lado_triangulo / 2,
        lado_triangulo,
        t,
        "white",
    )


draw_youtube(300, 200, 100)
turtle.exitonclick()
