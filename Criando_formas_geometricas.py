from msilib import change_sequence
import turtle
from turtle import onscreenclick, mainloop, onkey, listen
turtle = turtle.Turtle()

def square(start, end):
    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])

    width = max(diff_x, diff_y)

    for _ in range(4):
        turtle.forward(width)
        turtle.left(90)



def triangle(start, end):

    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])

    width = max(diff_x, diff_y)


    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)


def to_square():
    global shape
    shape = square

def to_rectangle():
    global shape
    shape = rectangle

def to_triangle():
    global shape
    shape = triangle

def to_line():
    global shape
    shape = line

def to_star():
    global shape
    shape = star

def rectangle(start, end):

    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])

    width = max(diff_x, diff_y)

    for _ in range(4):
        turtle.forward(200)
        turtle.left(90)



def line(start, end):
    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])

    width = max(diff_x, diff_y)
    turtle.forward(100)


def star(start, end):
    turtle.penup()
    turtle.goto(start[0], start[1])
    turtle.pendown()

    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])

    width = max(diff_x, diff_y)

    for _ in range(20):
        turtle.left(90)
        turtle.forward(100)
        turtle.left(10)
        turtle.backward(100)
        turtle.left(10)


def sol():
    for _ in range():
        turtle.circle()

#Estado
start = None
shape= square
   

def tap(x, y):
    global start
    if start is None:
        start = x, y

    else:
        end = x, y
        shape(start, end)
        start = None

def change_shape(next_shape):
    global shape
    shape = next_shape

onkey(lambda: change_shape(square), 's')
onkey(lambda: change_shape(rectangle), 'r')
onkey(lambda: change_shape(triangle), 't')
onkey(lambda: change_shape(line), 'l')
onkey(lambda: change_shape(star), 'S')

listen()
onscreenclick(tap)
mainloop()





