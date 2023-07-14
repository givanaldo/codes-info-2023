from turtle import *
penup()
setposition(-200, 0)
pendown()
bgcolor("yellow")
title("Desenhando sinais digitais")
shape("turtle")
fillcolor("red")
for _ in range(4):
    forward(50)
    left(90)
    for _ in range(2):
        forward(50)
        right(90)
    forward(50)
    left(90)

exitonclick()