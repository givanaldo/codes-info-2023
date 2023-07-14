import turtle
import random
import time

vetor = [1,2,3,4,5,6]

# criação das tartarugas
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)

player_two = turtle.Turtle()
player_two.color("blue")
player_two.shape("turtle")
player_two.penup()
player_two.goto(-200,-100)

player_three = turtle.Turtle()
player_three.color("purple")
player_three.shape("turtle")
player_three.penup()
player_three.goto(-200, 0)

# criação da chegada das tartarugas
player_one.setpos(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)

player_two.setpos(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

player_three.setpos(300,-40)
player_three.pendown()
player_three.circle(40)
player_three.penup()
player_three.goto(-200, 0)

# início da corrida
for i in range(20):
  if player_one.pos() >= (300, 100):
    player_one.write("Player One Wins!", font=("Arial", 20, "normal"))
    break
  elif player_two.pos() >= (300, -100):
    player_two.write("Player Two Wins!", font=("Arial", 20, "normal"))
    break
  elif player_three.pos() >= (300, 0):
    player_three.write("Player Three Wins!", font=("Arial", 20, "normal"))
    break
  else:
    velocidade = random.choice(vetor)
    player_one.forward(20*velocidade)
    velocidade = random.choice(vetor)
    player_two.forward(20*velocidade)
    velocidade = random.choice(vetor)
    player_three.forward(20*velocidade)
    time.sleep(1)

turtle.exitonclick()