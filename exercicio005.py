"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import turtle
import random # importar biblioteca 'random' para gerar números aleatórios

turtle = turtle.Turtle()
colors= ('#6A5ACD', '#00BFFF','#87CEEB', '#48D1CC','#F08080')

turtle.shape('turtle')
for _ in [1, 2, 3]:
    color = random.choice(colors) # a cor será escolhida aleatoriamente pela biblioteca 'random'
    turtle.color(color) 
    turtle.forward(100)
    turtle.right(120)

turtle.shape('circle')
for _ in [1, 2, 3, 4]:
  color = random.choice(colors)
  turtle.color(color)
  turtle.forward(200)
  turtle.right(90)
