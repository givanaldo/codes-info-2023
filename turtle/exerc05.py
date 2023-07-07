from turtle import *
penup()
setposition(-200, 0)
pendown()
for _ in range(3):
    forward(50)
    left(90)
    for _ in range(2):
        forward(50)
        right(90)
    forward(50)
    left(90)

exitonclick()