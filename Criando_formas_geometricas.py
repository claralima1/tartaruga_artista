import turtle

turtle = turtle.Turtle()

def square():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    
def triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def retangle():
    for _ in range(4):
        turtle.forward(200)
        turtle.left(90)

def line():
    turtle.forward(100)

turtle.color('blue')

def star():
    for _ in range(20):
        turtle.left(90)
        turtle.forward(100)
        turtle.left(10)
        turtle.backward(100)
        turtle.left(10)
       

star()




