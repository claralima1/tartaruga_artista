from turtle import *

from freegames import vector

class StatePen():
    def __init__(self, position_x, position_y):
        self.position = goto(position_x, position_y)

    def line(start, end):
        up()
        goto(start.x, start.y)
        goto(end.x, end.y)

    def tap( x, y):
        state = {'start': None, 'shape': None}
        start = state['start']
        state['start'] = None

        if start is None:
            state['start'] = vector(x, y)
        else:
            shape = state['shape']
            end = vector(x, y)
            shape(start, end)
    onscreenclick(tap)

    def store(key, value):
        state[key] = value

class Shapes():
    def __init__(self, position_x, position_y):
        self.position = goto(position_x, position_y)

    def square(start, end):
        up()
        goto(start.x, start.y)
        down()

        begin_fill()

        for count in range(4):
            forward(end.x - start.x)
            left(90)

        end_fill()

    def circle(start, end):
        up()
        goto(start.x, start.y)
        goto(end.x, end.y)
        down()

        begin_fill()

        for count in range(360):
            forward(end.x - start.x)
            left(1)

        end_fill() 

    def rectangle(start, end):
        up()
        goto(start.x, start.y)
        goto(end.x, end.y)
        down()

        begin_fill()

        for count in range(4):
            forward(end.x - start.x)
            forward(end.x - start.x)
            left(90)

        end_fill() 
    
    def triangle(start, end):
        up()
        goto(start.x, start.y)
        goto(end.x, end.y)
        down()

        begin_fill()

        for count in range(3):
            forward(end.x - start.x)
            left(120)

        end_fill() 

setup(420, 420, 370, 0)
     
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
done()
        
        