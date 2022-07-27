"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink','#00FF7F', '#008080']
for _ in range (8):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(200)
    turtle.backward(200)
    turtle.right(40)

for _ in range(18):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(200)
    turtle.backward(200)
    turtle.right(20)

