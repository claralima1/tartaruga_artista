from turtle import *

from freegames import vector

class StatePen:
    def __init__(self, start, end):
        self.start = state['start']

    def tap(self, x, y):
        if self.start is None:
            state['start'] = vector(x, y)
        else:
            shape = state['shape']
            self.end = vector(x, y)
            shape(self.start, self.end)
            state['start'] = None


 
def store(key, value):
    state[key] = value





class Shapes():
    def __init__(self):
       
        onkey(lambda: store(self.line()), 'l')  
        onkey(lambda: store(self.square()), 's')
        onkey(lambda: store(self.circle()), 'c')
        onkey(lambda: store(self.rectangle()), 'r')
        onkey(lambda: store(self.triangle()), 't')

    def line(self, start, end):
        up()
        goto(start.x, start.y)
        goto(end.x, end.y)
        down()

   

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

 
    state = {'start': None, 'shape': line()}    
onkey(undo, 'u')

def init():
    setup(420, 420, 370, 0)
    listen()
    mainloop()

if __name__ == '__main__':
    init()        
        