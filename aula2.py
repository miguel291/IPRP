import math

def problem_2():
    n_pessoas = 9
    tempo = 0
    while(n_pessoas <=60):
        n_pessoas+=2
        tempo+=5
    print("Demorou {} minutos".format(tempo))

def burger_exercise(square_side, circle_diameter):
    circle_area = math.pi * math.pow(circle_diameter/2,2)
    square_area = math.pow(square_side,2)
    if(circle_area > square_area):
        return("Circle is larger by {}%".format(((circle_area-square_area)/square_area)*100))
    else:
        return("Square is larger by {}%".format(((square_area-circle_area)/circle_area)*100))


def convert_cartesian_coordenates_to_polar(x,y):
    r = math.sqrt(math.pow(x,2)+math.pow(y,2))
    if (x == 0):
        if(y > 0):
            return(r,math.pi/2)
        elif(y < 0):
            return(r,-math.pi/2)
        else:
            return(r,0)
    else:
        return(r,math.atan(y/x))

def indice_massa_corporal_calculator(peso,altura):
    return("O seu indice de massa corporal é: " + str(round(peso/math.pow(altura,2),2)))


if __name__ == '__main__':
    print(convert_cartesian_coordenates_to_polar(-1,1))
    print(burger_exercise(7.62,8.89))
    print(indice_massa_corporal_calculator(90,1.91))
    print(convert_cartesian_coordenates_to_polar(0,1))
