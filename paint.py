"""Paint, for drawing shapes.

Exercises

1. Add a color.
ss3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import pensize, setup, onkey, onscreenclick, listen, up, goto, down, begin_fill, end_fill, done, undo, forward, backward, left, right, color
from freegames import vector
  

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
    pensize(50)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()

    begin_fill()#inicio do preenchimento

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill() #final do preenchimento


def circle(start, end):
    """Draw circle from start to end."""
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
    """Draw rectangle from start to end."""
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
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    goto(end.x, end.y)
    down()

    begin_fill()

    for count in range(3):
        forward(end.x - start.x)

        left(120)

    end_fill() 

def flor(start, end):
    up()
    goto(start.x, start.y)
    goto(end.x, end.y)
    down()

    begin_fill()

    for count in range(80):
        forward(end.x - start.x)
        backward(end.x - start.x)
        left(5)

    end_fill() 

def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None



def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
setup(420, 420, 370, 0)
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('pink'), 'p')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', flor), 'f')
done()
