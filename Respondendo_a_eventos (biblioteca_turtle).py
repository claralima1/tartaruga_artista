from turtle import onkey, listen, Turtle

turtle = Turtle()


def up():
    y_atual = turtle.ycor()
    novo_y = y_atual + 5
    turtle.sety(novo_y)



def down():
	y_atual = turtle.ycor()
	novo_y = y_atual - 5
	turtle.sety(novo_y)



def left():
	x_atual = turtle.xcor()
	novo_x = x_atual + 5
	turtle.setx(novo_x)

def rigth():
	x_atual = turtle.xcor()
	novo_x = x_atual + 5
	turtle.setx(novo_x)

onkey(rigth, 'Right')
onkey(left, 'Left')
onkey(down, 'Down')
onkey(up, 'Up')

listen()