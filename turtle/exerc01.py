from turtle import *
fillcolor('red')
begin_fill()
penup()
setposition(-300,0)
pendown()
for _ in range(4):
    forward(100)
    left(90)
end_fill()

fillcolor('blue')
begin_fill()
penup()
setposition(-100,0)
pendown()
for _ in range(5):
    forward(120)
    left(72)
end_fill()

fillcolor('yellow')
begin_fill()
penup()
setposition(200,0)
pendown()
for _ in range(8):
    forward(120)
    left(45)
end_fill()

exitonclick()