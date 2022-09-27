import math
import turtle

def minimum_number_of_bottles(litros):
    result = []
    bottles = [5, 1.5, 0.5,0.25]
    i = 0
    while(litros > 0 & i!= len(bottles)-1):
        result.append(0)
        while(litros >= bottles[i]):
            litros -= bottles[i]
            result[i] += 1
        i+=1
    if(litros > 0):
            result[i] += 1

    return "São precisas {} garrafas de 5 litros, {} garrafas de 1.5 litros, {} garrafas de 0.5 litros e {} garrafas de 0.25 litros".format(result[0], result[1],result[2],result[3])

def draw_increasing_sided_star(angle):
    colors = ["purple","blue","yellow"]
    joao = turtle.Turtle()
    joao.setposition(0,0)
    joao.speed(0)
    for i in range (2000):
        joao.color(colors[i%3])
        joao.forward(i/2)
        joao.right(angle)
    turtle.done()

if __name__ == '__main__':
    print(minimum_number_of_bottles(0.25))
    draw_increasing_sided_star(85)