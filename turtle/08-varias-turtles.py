import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.penup()
t1.setpos(-100, 100)
t1.pendown()
t1.fillcolor('red')
for _ in range(4):
    t1.forward(100)
    t1.left(90)

t2.penup()
t2.setpos(-100, -100)
t2.pendown()
t2.fillcolor('yellow')
t2.circle(100)

turtle.exitonclick()