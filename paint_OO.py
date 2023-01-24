import turtle
from turtle import *
from freegames import vector

class Shape:
  state={'start': None, 'shape': 'line'}
 
  def __init__(self):
    self.start=None
    self.end=None
       
  def tap (self,x,y):  
    start = self.state['start']

    if start is None:
      self.state['start'] = vector(x, y)

    else:
      end = vector(x, y)
      self.draw(start, end)
      self.state['start'] = None

  def listen(self):
    turtle.listen()
    turtle.onkey(lambda: turtle.color('black'), 'K')
    turtle.onkey(lambda: turtle.color('white'), 'W')
    turtle.onkey(lambda: turtle.color('green'), 'G')
    turtle.onkey(lambda: turtle.color('blue'), 'B')
    turtle.onkey(lambda: turtle.color('red'), 'R')
    turtle.onkey(lambda: turtle.onscreenclick(square.tap), 's')
    turtle.onkey(lambda: turtle.onscreenclick(circle.tap), 'c')
    turtle.onkey(lambda: turtle.onscreenclick(rectangle.tap), 'r')
    turtle.onkey(lambda: turtle.onscreenclick(triangle.tap), 't')
    turtle.onkey(lambda: turtle.onscreenclick(line.tap), 'l')
    turtle.done()

class Line(Shape):
    def __init__(self):
        super().__init__()
        
    def draw(self, start, end):
        turtle.up()
        turtle.goto(start.x, start.y)
        turtle.down()
        turtle.goto(end.x, end.y)

class Triangle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self, start, end):
        turtle.up()
        turtle.goto(start.x, start.y)
        turtle.goto(end.x, end.y)
        turtle.down()

        turtle.begin_fill()
        for count in range(3):
            turtle.forward(end.x - start.x)
            turtle.left(120)
        turtle.end_fill() 

class Square(Shape):
    def __init__(self):
        super().__init__()

    def draw(self, start, end):
        turtle.up()
        turtle.goto(start.x, start.y)
        turtle.down()

        turtle.begin_fill()
        for count in range(4):
            turtle.forward(end.x - start.x)
            turtle.left(90)
        turtle.end_fill()

class Circle(Shape):
    def __init__(self):
        super().__init__()

    def draw(self, start, end):
        turtle.up()
        turtle.goto(start.x, start.y)
        turtle.goto(end.x, end.y)
        turtle.down()

        turtle.begin_fill()
        for count in range(360):
            turtle.forward(end.x - start.x)
            turtle.left(1)
        turtle.end_fill()

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
    
    def draw(self, start, end):
        turtle.up()
        turtle.goto(start.x, start.y)
        turtle.goto(end.x, end.y)
        turtle.down()

        turtle.begin_fill()
        for count in range(4):
            turtle.forward(end.x - start.x)
            turtle.forward(end.x - start.x)
            turtle.left(90)
        turtle.end_fill() 
        
shape = Shape()
line = Line()
triangle = Triangle() 
square = Square()
circle = Circle()
rectangle = Rectangle()
turtle.setup(420, 420, 370, 0)
turtle.onscreenclick(line.tap)  
shape.listen()