import turtle
import random
import time

vetor = [1,2,3,4,5,6]

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

for i in range(20):
  if player_one.pos() >= (300,100):
    turtle.write("Player One Wins!", font=("Arial", 15, "normal"))
    break
  elif player_two.pos() >= (300,-100):
    turtle.write("Player Two Wins!", font=("Arial", 15, "normal"))
    break
  else:
    velocidade = random.choice(vetor)
    player_one.forward(20*velocidade)
    velocidade = random.choice(vetor)
    player_two.forward(20*velocidade)
    time.sleep(1)

turtle.exitonclick()