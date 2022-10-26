from turtle import *

from freegames import vector

class Caneta():
    def __init__(self, start_x, start_y):
        self.position = goto(start_x, start_y)
    
    def line(start, end):
        up()
        goto(start.x, start.y)
        down()
        goto(end.x, end.y)

        

    def tap(self, x, y):

        self.state = {'start': None, 'shape': line}
        self.start = self.state['start']
        self.state['start'] = None

        if self.start is None:
            self.state['start'] = vector(x, y)
        else:
            self.shape = self.state['shape']
            self.end = vector(x, y)
            shape(self.start, self.end)
    onscreenclick(tap) 
    



setup(420, 420, 370, 0)
     
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
done()
        
        