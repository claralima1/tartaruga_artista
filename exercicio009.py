"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle
import random

turtle = turtle.Turtle()
colors = ['purple', 'blue', 'orange', 'green', 'pink', '#00FF7F', '#008080']

for c in range(360):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(3)
    turtle.right(1)
