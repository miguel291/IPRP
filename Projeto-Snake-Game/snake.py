"""Trabalho realizado por Miguel Pedroso 2019218176
no âmbito da cadeira de IPRP na Universidade de Coimbra"""

import time
import random
import functools
import turtle
import math
import os

MAX_X = 600
MAX_Y = 800
DEFAULT_SIZE = 20
SNAKE_SHAPE = "square"
HIGH_SCORES_FILE_PATH = "high_scores.txt"
# Controla a velocidade da cobra. Quanto menor o valor, mais rápido é o movimento da cobra.
SPEED = 0.1


def load_high_score(state):
    # se já existir um high score devem guardar o valor em state['high_score']
    full_path = os.path.realpath(__file__)
    file_path = os.path.dirname(full_path) + "/" + HIGH_SCORES_FILE_PATH
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as high_scores_file:
            state["high_score"] = (int)(high_scores_file.readlines()[-1])
        high_scores_file.close()
    pass


def write_high_score_to_file(state):
    # devem escrever o valor que está em state['high_score'] no ficheiro de high scores
    full_path = os.path.realpath(__file__)
    file_path = os.path.dirname(full_path) + "/" + HIGH_SCORES_FILE_PATH
    high_scores_file = open(file_path, "a", encoding="utf-8")
    high_scores_file.write(str(state["high_score"]) + "\n")
    high_scores_file.close()
    pass


def create_score_board(state):
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.shape("square")
    score_board.color("black")
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, MAX_Y / 2.2)
    state["score_board"] = score_board
    load_high_score(state)
    update_score_board(state)


def update_score_board(state):
    state["score_board"].clear()
    state["score_board"].write(
        "Score: {} High Score: {}".format(state["score"], state["high_score"]),
        align="center",
        font=("Helvetica", 24, "normal"),
    )


def go_up(state):
    if state["snake"]["current_direction"] != "down":
        state["snake"]["current_direction"] = "up"


def go_down(state):
    if state["snake"]["current_direction"] != "up":
        state["snake"]["current_direction"] = "down"


def go_left(state):
    if state["snake"]["current_direction"] != "right":
        state["snake"]["current_direction"] = "left"


def go_right(state):
    if state["snake"]["current_direction"] != "left":
        state["snake"]["current_direction"] = "right"


def init_state():
    state = {}
    # Informação necessária para a criação do score board
    state["score_board"] = None
    state["new_high_score"] = False
    state["high_score"] = 0
    state["score"] = 0
    # Para gerar a comida deverá criar um nova tartaruga e colocar a mesma numa posição aleatória do campo
    state["food"] = None
    state["window"] = None
    snake = {
        "head": None,  # Variável que corresponde à cabeça da cobra
        "current_direction": None,  # Indicação da direcção atual do movimento da cobra
        "body": [],
    }
    state["snake"] = snake
    state["new_body_part"] = False
    return state


def setup(state):
    window = turtle.Screen()
    window.setup(width=MAX_X, height=MAX_Y)
    window.listen()
    window.onkey(functools.partial(go_up, state), "w")
    window.onkey(functools.partial(go_down, state), "s")
    window.onkey(functools.partial(go_left, state), "a")
    window.onkey(functools.partial(go_right, state), "d")
    window.tracer(0)
    state["window"] = window
    snake = state["snake"]
    snake["current_direction"] = "right"
    snake["head"] = turtle.Turtle()
    snake["head"].shape(SNAKE_SHAPE)
    snake["head"].showturtle()
    snake["head"].pu()
    snake["head"].color("green")
    create_score_board(state)
    create_food(state)


def generate_random_position():
    """
    Função que cria as coordenadas para a comida
    """
    x = random.randint(-MAX_X / 2 + 20, MAX_X / 2 - 20)
    y = random.randint(-MAX_Y / 2 + 20, MAX_Y / 2 - 20)
    return x, y


def move(state):
    """
    Função responsável pelo movimento da cobra no ambiente.
    """
    snake = state["snake"]
    new_body_part = None
    # Se a cobra tiver comido cria nova parte do corpo
    if state["new_body_part"]:
        new_body_part = create_body_part(state)
        state["new_body_part"] = False

    # A direção de cada parte da cobra é a direção da parte que lhe antecede no corpo
    for index, body_part in reversed(list(enumerate(snake["body"]))):
        if index == 0:
            dict_direction = {90: "up", 270: "down", 0: "right", 180: "left"}
            direction = dict_direction.get(snake["head"].heading())
            body_part[1] = direction
        else:
            body_part[1] = snake["body"][index - 1][1]

    direction_dict = {"up": 90, "down": -90, "left": 180, "right": 0}
    snake["head"].setheading(direction_dict.get(snake["current_direction"]))
    snake["head"].forward(DEFAULT_SIZE)

    for body_part in snake["body"]:
        body_part[0].setheading(direction_dict.get(body_part[1]))
        body_part[0].forward(DEFAULT_SIZE)
    # Adiciona a parte do corpo criada à lista body, caso tenha sido criada
    if new_body_part is not None:
        snake["body"].append(new_body_part)


def create_food(state):
    """
    Função responsável pela criação da comida. Note que elas deverão ser colocadas em posições aleatórias, mas dentro dos limites do ambiente.
    """
    # a informação sobre a comida deve ser guardada em state['food']
    if state["food"] is None:
        x, y = generate_random_position()
        state["food"] = turtle.Turtle()
        state["food"].penup()
        state["food"].setposition(x, y)
        state["food"].pendown()
        state["food"].shape("circle")
        state["food"].color("red")


def create_body_part(state):
    """
    Função responsável pela criação de novas partes do corpo.
    """
    snake = state["snake"]
    new_body_part = turtle.Turtle()
    new_body_part.shape(SNAKE_SHAPE)
    new_body_part.showturtle()
    new_body_part.pu()
    new_body_part.color("black")
    # caso a cobra tenha cabeça e pelo menos uma parte do corpo
    if snake["body"]:
        direction = snake["body"][-1][1]
        new_body_part.setposition(snake["body"][-1][0].position())
    # caso só exista a cabeça
    else:
        dict_direction = {90: "up", 270: "down", 0: "right", 180: "left"}
        direction = dict_direction.get(snake["head"].heading())
        new_body_part.setposition(snake["head"].position())
    return [new_body_part, direction]


def check_if_food_to_eat(state):
    """
    Função responsável por verificar se a cobra tem uma peça de comida para comer. Deverá considerar que se a comida estiver a uma distância inferior a 15 pixels a cobra pode comer a peça de comida.
    """
    food = state["food"]
    snake_head = state["snake"]["head"]
    if (
        math.sqrt(
            math.pow(snake_head.ycor() - food.ycor(), 2)
            + math.pow(snake_head.xcor() - food.xcor(), 2)
        )
        < 15
    ):
        state["food"].hideturtle()
        state["food"] = None
        state["score"] += 10
        create_food(state)
        update_score_board(state)
        state["new_body_part"] = True
    # para ler ou escrever os valores de high score, score e new high score, devem usar os respetivos campos do state: state['high_score'], state['score'] e state['new_high_score']


def boundaries_collision(state):
    """
    Função responsável por verificar se a cobra colidiu com os limites do ambiente. Sempre que isto acontecer a função deverá returnar o valor booleano True, caso contrário retorna False.
    """
    snake = state["snake"]
    x_cor = snake["head"].xcor()
    y_cor = snake["head"].ycor()
    # print("x: " + str(x_cor) + " y: " + str(y_cor))
    # Verifica se a cabeça da cobra está numa posição fora dos limites do ambiente
    if (
        x_cor > (MAX_X / 2 - 10)
        or x_cor < (-MAX_X / 2 + 10)
        or y_cor > (MAX_Y / 2 - 10)
        or y_cor < (-MAX_Y / 2 - 10)
    ):
        return True
    return False


def check_collisions(state):
    """
    Função responsável por avaliar se há colisões. Atualmente apenas chama a função que verifica se há colisões com os limites do ambiente. No entanto deverá escrever o código para verificar quando é que a tartaruga choca com uma parede ou com o seu corpo.
    """
    snake = state["snake"]
    boundary_collision = boundaries_collision(state)
    if boundary_collision:
        return True
    for body_part in snake["body"]:
        # print(body_part[0].pos() - snake['head'].pos())
        if (abs(body_part[0].xcor() - snake["head"].xcor()) < (1)) and (
            abs(body_part[0].ycor() - snake["head"].ycor()) < (1)
        ):
            return True
    return False


def main():
    state = init_state()
    setup(state)
    while not check_collisions(state):
        state["window"].update()
        check_if_food_to_eat(state)
        move(state)
        time.sleep(SPEED)
    print("YOU LOSE!")
    if state["score"] > state["high_score"]:
        state["high_score"] = state["score"]
        write_high_score_to_file(state)


main()
