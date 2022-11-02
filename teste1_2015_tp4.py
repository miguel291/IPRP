import turtle
import random

def draw_circle(x,y,radius,color):
    turt = turtle.Turtle()
    turt.speed(10)
    turtle.colormode(255)
    turt.penup()
    turt.goto(x,y)
    turt.pendown()
    turt.pencolor(color)
    turt.fillcolor(color)
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()
    turt.hideturtle()
    
def draw_mickey(x,y,size,color):
    draw_circle(x,y,size*40,color)
    draw_circle(x-size*40,size*1.5*40+y,size*20,color)
    draw_circle(x+size*40,size*1.5*40+y,size*20,color)
    

def draw_many_mickeys(number):
    colors = ['red','green','yellow','purple','blue','black','pink','orange','brown']
    for i in range(number):
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        size = random.uniform(0.5,2)
        draw_mickey(x,y,size,color)
        
        
draw_many_mickeys(10)
turtle.exitonclick()
    