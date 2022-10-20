"""Code made in lesson 7 of IPRP course @UniveristyOfCoimbra."""

import turtle
import numpy as np
import math


def polar_to_carthesian_coordinates(rho, phi):
    """Converts polar to carthesian coordinates"""
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return (x, y)


def draw_radioactivity_sign(turt):
    """Uses the turte module to draw the radioactivity sign"""
    colors = ["Yellow", "Black", "Blue"]
    turt = turtle.Turtle()
    turt.speed(10000000000000)
    for i in range(1000):
        if i < 50:
            turt.color("black")
        elif i < 340:
            turt.color(colors[i % 2])
        else:
            turt.color("Yellow")
        turt.forward(1 * i)
        turt.right(60)


def draw_circle_with_turtle(turt, x, y, radius, color):
    """ "Draws a circle using the turtle module"""
    turt.width(4)
    turt.color(color)
    turt.speed(1000)
    turt.penup()
    turt.goto(x, y)
    turt.forward(radius)
    turt.right(90)
    turt.pendown()
    for i in range(360):
        turt.forward(0.5)
        turt.right(1)
    turt.hideturtle()


def draw_nautilus_with_turtle(turt, radius):
    """ "Draws a nautilus using the turtle module"""
    turt.speed(1000)
    turt.penup()
    turt.left(radius)
    turt.pendown()
    for i in range(4):
        turt.forward(radius * 4)
        turt.right(90)
    turt.hideturtle()


def leave_trail(turt):
    """Turtle leaves a circular trail on a blue screen"""
    turt.speed(1000)
    turtle.Screen().bgcolor("blue")
    turt.color("red")
    for i in range(200):
        turt.penup()
        turt.fd(i * 2)
        turt.stamp()
        turt.left(20)


def draw_form(turt, num_sides, length, angle, x, y):
    """Uses turtle to draw a yellow form"""
    turt.speed(1000)
    turt.fillcolor("yellow")
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    for i in range(num_sides):
        turt.fd(length)
        turt.right(angle)
    turt.end_fill()


def growing_5_sided_star(turt, length,):
    """Uses turtle to draw a yellow 5-sided star"""
    turt.speed(10)
    for i in range(200):
        turt.fd(length + 2 * i)
        turt.right(180 - 36)
        turt.fd(length + 2 * i)
        turt.left(72)
    turt.end_fill()


def draw_5_sided_star(turt, length, x, y):
    """Uses turtle to draw a yellow 5-sided star"""
    turt.speed(10)
    turt.fillcolor("yellow")
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.begin_fill()
    for i in range(5):
        turt.fd(length)
        turt.right(180 - 36)
        turt.fd(length)
        turt.left(72)
    turt.end_fill()


def european_union_flag(turt):
    """Uses turtle to draw European Union flag"""
    turt.speed(1000)
    turtle.Screen().bgcolor("blue")
    for i in range(12):
        angle = math.radians(i * 360 / 12)
        x, y = polar_to_carthesian_coordinates(250, angle)
        draw_5_sided_star(turt, 20, x, y)
    turt.hideturtle()


if __name__ == "__main__":
    # draw_circle_with_turtle(turtle.Turtle(),0,0,3,"Black")
    # draw_circle_with_turtle(turtle.Turtle(),-60,0,3,"Blue")
    # draw_circle_with_turtle(turtle.Turtle(),60,0,3,"Red")
    # draw_circle_with_turtle(turtle.Turtle(),-30,-25,3,"Yellow")
    # draw_circle_with_turtle(turtle.Turtle(),30,-25,3,"Green")
    joao = turtle.Turtle()
    # leave_trail(joao)
    # european_union_flag(joao)
    growing_5_sided_star(joao, 5)
    # draw_5_sided_star(joao ,20, 0,0)
    turtle.done()
