from turtle import *

from freegames import vector

class Shapes:
    def __init__(self):
        self.tap()
        self.store()
        self.drawn()

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


state = {'start': None, 'shape': line}

class line(Shapes):
    def __init__(self, start, end):
        up()
        goto(start.x, start.y)
        down()
        goto(end.x, end.y)



        