"""Code made in lesson 9 of IPRP course @UniveristyOfCoimbra."""

import turtle


def draw_radioactive_triangle(turt, x, y, size, heading):
    """Draws the radioactive sign "triangle" using turtle"""
    turt.fillcolor("Black")
    turt.penup() 
    turt.goto(x, y)
    turt.setheading(heading)
    turt.pendown()
    turt.begin_fill()
    turt.fd(size)
    turt.left(90)
    turt.circle(size, 60)
    turt.left(90)
    turt.fd(size)
    turt.end_fill()
    
    
def draw_radioactivity_sign(turt):
    """Uses the turte module to draw the radioactivity sign"""
    turtle.Screen().bgcolor("Yellow")
    for i in range(3):
        draw_radioactive_triangle(turt, 0, 0, 300, i*120)
    turt.setheading(0)
    turt.penup()
    turt.goto(0,-100)
    turt.pendown()
    turt.begin_fill()
    turt.color("Yellow")
    turt.circle(100)
    turt.fillcolor("Black")
    turt.end_fill()
    turt.hideturtle()

def draw_nautilus_with_turtle(turt, radius, expansion):
    """ "Draws a nautilus using the turtle module"""
    turt.speed(1000)
    turt.penup()
    turt.left(radius)
    turt.pendown()
    for i in range(expansion): 
        move = radius * (i + 1)
        for i in range(4):
            turt.forward(move * 6)
            turt.left(90)
        turt.left(5)
    turt.hideturtle()


def draw_circle_with_turtle(turt, x, y, radius, color):
    """ "Draws a circle using the turtle module"""
    turt.width(4)
    turt.color(color)
    turt.speed(1000)
    turt.setheading(0)
    turt.penup()
    turt.goto(x, y)
    turt.forward(radius)
    turt.right(90)
    turt.pendown()
    for i in range(360):
        turt.forward(0.5)
        turt.right(1)
    turt.hideturtle()

if __name__ == "__main__":
    i = 0
    joao = turtle.Turtle()
    joao.speed(10)
    #draw_circle_with_turtle(joao,0,0,3,"Black")
    #draw_circle_with_turtle(joao,-65,0,3,"Blue")
    #draw_circle_with_turtle(joao,65,0,3,"Red")
    #draw_circle_with_turtle(joao,-33,-30,3,"Yellow")
    #draw_circle_with_turtle(joao,33,-30,3,"Green")
    #draw_nautilus_with_turtle(joao, 1, 30);
    draw_radioactivity_sign(joao)
    turtle.done()