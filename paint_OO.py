import turtle
from turtle import *
from freegames import vector

#Classe Line
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
      #shape = self.state['shape']
      end = vector(x, y)
      self.draw(start, end)
      self.state['start'] = None

  def listen(self):
    turtle.listen()
    turtle.onkey(lambda: turtle.color('black'), 'K')#botão para mudar de cor
    turtle.onkey(lambda: turtle.color('white'), 'W')#botão para mudar de cor
    turtle.onkey(lambda: turtle.color('green'), 'G')#botão para mudar de cor
    turtle.onkey(lambda: turtle.color('blue'), 'B')#botão para mudar de cor
    turtle.onkey(lambda: turtle.color('red'), 'R')#botão para mudar de cor
    turtle.onkey(lambda: turtle.color('purple'), 'P')#botão para mudar de cor
    turtle.onkey(lambda: turtle.color('orange'), 'O')#botão para mudar de cor
    turtle.onkey(lambda: triangle.draw(), 't')
    turtle.onkey(lambda: square.draw(), 's')
    turtle.onkey(lambda: circle.draw(), 'c')
    turtle.onkey(lambda: rectangle.draw(), 'r')
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
        turtledown()

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

line = Line()
shape = Shape()
triangle = Triangle() 
square = Square()
circle = Circle()
rectangle = Rectangle()
turtle.setup(420, 420, 370, 0)
turtle.onscreenclick(line.tap) 
shape.listen()