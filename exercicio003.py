"""
Exercícios

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""

import turtle

turtle = turtle.Turtle()

turtle.shape('turtle')
turtle.pensize(50) #espessura da caneta

for color in [ 'black','blue', 'pink', 'red']: #lista de cores 
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)

turtle.up() # caneta para cima
turtle.forward(200)
turtle.down() # caneta para baixo

for color in [ '#6A5ACD','#1E90FF', '#87CEEB', '#00CED1']: #lista de cores 
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)
