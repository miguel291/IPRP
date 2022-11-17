"Code made in lesson 12"
import os
import datetime
import random
import turtle


def first_file():
    "Create a file with the current date and time"
    with open(
        os.path.dirname(full_path) + "/primeiro.txt", "w", encoding="utf-8"
    ) as primeiro:
        text = "Acabei de criar o meu primeiro ficheiro em Python."
        primeiro.write(text)

        primeiro.write("\n")
        primeiro.write(str(datetime.datetime.now()))
        primeiro.close()


def copy_file(original_name, copy_name):
    "Copies a file"

    with open(original_name, "r", encoding="utf-8") as original, open(
        copy_name, "w", encoding="utf-8"
    ) as copy:
        copy.write(original.read())
        original.close()
        copy.close()


def generate_random_numbers():
    "Generates a random number between -6 and 6"
    return random.randint(-6, 6)


def create_file_pair_random_numbers(name, lines):
    "Creates a file with a pair of random numbers per line"
    with open(name, "w", encoding="utf-8") as file:
        for i in range(lines):
            file.write(
                str(generate_random_numbers())
                + " "
                + str(generate_random_numbers())
                + "\n"
            )
    file.close()


def read_file_pair_random_numbers(name):
    "Reads a file that has a pair of random numbers per line"
    coordinates_list = []
    with open(name, "r", encoding="utf-8") as file:
        while file.readline() != "":
            line = file.readline().split(" ")
            coordinates_list.append(int(line[0]))
            coordinates_list.append(int(line[1]))
    return coordinates_list


def draw_turtle_coordinates(coordinates_list):
    "Gets a list of coordinates and draws them using turtle"
    t = turtle.Turtle()
    if len(coordinates_list) % 2 != 0:
        print("Erro: A lista de coordenadas não é par.")
        return
    for i in range(0, len(coordinates_list), 2):
        t.goto(coordinates_list[i] * 50, coordinates_list[i + 1] * 50)


if __name__ == "__main__":
    full_path = os.path.realpath(__file__)
    # original = input("Introduza o nome do ficheiro original: ")
    # copy = input("Introduza o nome do ficheiro de cópia: ")
    # copy_file(os.path.dirname(full_path) + '/' + original, os.path.dirname(full_path) + '/' + copy)

    create_file_pair_random_numbers(
        os.path.dirname(full_path) + "/random_numbers.txt", 10
    )
    random_coordinates = read_file_pair_random_numbers(
        os.path.dirname(full_path) + "/random_numbers.txt"
    )
    print(random_coordinates)
    draw_turtle_coordinates(random_coordinates)
    turtle.exitonclick()
