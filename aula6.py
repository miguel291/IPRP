"""Code made in lesson 6 of IPRP course @UniveristyOfCoimbra."""

import random
import turtle


def print_dumb_pyramid(rows):
    """Prints a dumb pyramid"""
    """1
       1 2
       1 2 3"""
    j = 0
    for i in range(rows):
        j = j + 1
        for m in range(j):
            print(m + 1, end=" ")
            m = m + 1
        print("")


def print_dumb_pyramid_version_b(rows):
    """Prints a dumb pyramid as well"""
    j = rows
    for i in range(rows):
        for m in range(j):
            print(m + 1, end=" ")
            m = m + 1
        print("")
        j = j - 1


def print_dumb_pyramid_version_c(rows):
    """Prints the last dumb pyramid"""
    for i in range(rows):
        number_blank_spaces = rows - i - 1
        for m in range(number_blank_spaces):
            print("  ", end="")
        for j in range(i + 1):
            print(i - j + 1, end=" ")
        print("")


def calculate_factorial(num):
    """Calculates the factorial of a number"""
    result = 1
    for i in range(num):
        result = result * (i + 1)
    return result


def calculate_natural_logarithm(limit):
    """Approximates the natural logarithm value given a certain precision(limit)"""
    e = 0
    for i in range(limit):
        e = e + (1 / calculate_factorial(i))
    print("e is approximately :" + str(e))


def throw_die_and_calculate_percentage_of_even_throws(number_of_throws):
    """Throws 6-sided die"""
    even_throws = 0
    odd_throws = 0
    for i in range(number_of_throws):
        throw = random.randrange(1, 7)
        print("Throw number: {0}: {1}".format(i + 1, throw))
        if throw % 2 == 0:
            even_throws += 1
        else:
            odd_throws += 1
    print(100 * even_throws / (even_throws + odd_throws))


def replace_while_with_for_cycle():
    """Replace the below code witha for cycle
    i = 20
    while (i >= 0):
    print( "i= ",i) i=i-2
    """
    for i in range(20, -1, -2):
        print("i= ", i)


def check_if_words_are_friends(word1, word2):
    """Check if two words are 90% or more equal"""
    word1 = word1.lower()
    word2 = word2.lower()
    equal_letters = 0
    different_letters = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            different_letters += 1
        else:
            equal_letters += 1
    if equal_letters / (equal_letters + different_letters) >= 0.9:
        print("The words are friends")
    else:
        print("The words are not friends")


def draw_radioactivity_sign():
    """Uses the turte module to draw the radioactivity sign"""
    colors = ["Yellow", "Black", "Blue"]
    joao = turtle.Turtle()
    joao.speed(10000000000000)
    for i in range(1000):
        if i < 50:
            joao.color("black")
        elif i < 340:
            joao.color(colors[i % 2])
        else:
            joao.color("Yellow")
        joao.forward(1 * i)
        joao.right(60)


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


if __name__ == "__main__":
    # print_dumb_pyramid(5)
    # print("-------------------")
    # print_dumb_pyramid_version_b(5)
    # print("-------------------")
    # print_dumb_pyramid_version_c(5)
    # print(calculate_factorial(5))
    # calculate_natural_logarithm(1000)
    # throw_die_and_calculate_percentage_of_even_throws(10)
    # replace_while_with_for_cycle()
    # check_if_words_are_friends("ola", "adeus")
    # check_if_words_are_friends("qwertyaeiou", "qwertzaeiou")
    # draw_circle_with_turtle(turtle.Turtle(),0,0,3,"Black")
    # draw_circle_with_turtle(turtle.Turtle(),-60,0,3,"Blue")
    # draw_circle_with_turtle(turtle.Turtle(),60,0,3,"Red")
    # draw_circle_with_turtle(turtle.Turtle(),-30,-25,3,"Yellow")
    # draw_circle_with_turtle(turtle.Turtle(),30,-25,3,"Green")
    joao = turtle.Turtle()
    for i in range(20):
        draw_nautilus_with_turtle(joao, i)
    turtle.done()
