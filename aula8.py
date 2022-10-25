"""Code made in lesson 8 of IPRP course @UniveristyOfCoimbra."""

import turtle


def draw_smile(t, face_radius, eye_radius):
    """Draw a smiley face."""
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.circle(face_radius)
    t.penup()
    t.goto(-40, 150)
    t.dot(eye_radius, "blue")
    t.goto(40, 150)
    t.dot(eye_radius, "blue")
    t.goto(100, 0)
    t.setheading(30)
    t.pendown()
    t.circle(face_radius, -70)


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


if __name__ == "__main__":
    joao = turtle.t()
    joao.speed(10)
    # draw_smile(joao, 200, 40)
    draw_radioactivity_sign(joao)
    turtle.done()
