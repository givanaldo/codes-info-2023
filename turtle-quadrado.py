import turtle

t = turtle.Turtle()
tamanho = 300
t.penup()
t.goto(-100, -100)
t.pendown()
t.forward(tamanho)
t.left(90)
t.forward(tamanho)
t.left(90)
t.forward(tamanho)
t.left(90)
t.forward(tamanho)
t.left(90)

janela = turtle.Screen()
janela.exitonclick()