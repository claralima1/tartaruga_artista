from turtle import *
t = Turtle()

from freegames import vector


class Shapes:
    def __init__(self):
        self.state = {'start': None, 'shape': l.drawn()}

    def tap(self, x, y):

        self.start = state['start']

        if start is None:
            self.state['start'] = vector(self.x, self.y)
        else:
            self.shape = state['shape']
            self.end = vector(self.x, self.y)
            self.shape(self.start, self.end)
            self.state['start'] = None

    def store(key, value):
        self.state[key] = value
        
s = Shapes()
onscreenclick(s.tap())

class Line(Shapes):
    def __init__(self):
        self.state = {'start': None, 'shape': self.l.drawn()}
        
    def drawn(self, start, end):
        self.t.up()
        self.t.goto(self.start.x, self.start.y)
        self.t.down()
        self.t.goto(self.end.x, self.end.y)
            
l = Line()
setup(420, 420, 370, 0)
listen()
done()


        