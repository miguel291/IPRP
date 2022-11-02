import turtle

"""Usando o módulo turtle, escreva um programa que lhe permita desenhar a figura ilustrada em 1,
que representa uma cortina de uma janela. O programa deverá ser parametrizável para
permitir desenhar um número variável de ’ondas’ na cortina bem como a altura e a largura da mesma.
Serão valorizadas soluções modulares.
"""


def desenhar_onda(raio_onda, turt, direcao):
    turt.setheading(-90)
    if direcao == 1:
        angulo = -180
    else:
        angulo = 180
    turt.circle(raio_onda, angulo)


def desenhar_cortina(num_ondas, altura, largura):
    raio_onda = largura / (num_ondas * 2)
    turt = turtle.Turtle()
    turt.penup()
    turt.goto(-largura / 2, altura)
    turt.pendown()
    turt.right(90)
    turt.fd(altura)
    for i in range(num_ondas):
        direcao = i % 2
        desenhar_onda(raio_onda, turt, direcao)
    turt.setheading(0)
    turt.left(90)
    turt.fd(altura)
    turt.left(90)
    turt.fd(largura)
    turt.hideturtle()


if __name__ == "__main__":
    desenhar_cortina(10, 100, 200)
    turtle.exitonclick()
