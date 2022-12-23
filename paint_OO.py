from turtle import *

from freegames import vector

class StatePen:
    def __init__(self, position_x, position_y):
        self.position = goto(position_x, position_y)

    def line(start, end):
        up()
        goto(start.x, start.y)
        goto(end.x, end.y)

    def tap(x, y):
        start = state['start']

        if start is None:
            state['start'] = vector(x, y)
        else:
            shape = state['shape']
            end = vector(x, y)
            shape(start, end)
            state['start'] = None


def store(key, value):
    state[key] = value

s = StatePen()
state = {'start': None, 'shape': s.line()}



class Shapes():
    def __init__(self):
        self.position = goto()

   

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

def init():
    setup(420, 420, 370, 0)
    listen()
    done()

if __name__ == '__main__':
    init()
     
onkey(undo, 'u')
class PenColor:
    def __init__ (self):
        
        onkey(lambda: store('shape', s.line()), 'l')
        onkey(lambda: store('shape', s.square()), 's')
        onkey(lambda: store('shape', s.circle()), 'c')
        onkey(lambda: store('shape', s.rectangle()), 'r')
        onkey(lambda: store('shape', s.triangle()), 't')

        
        