class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):

        '''
        Retorne  representação textual no formato (x, y)
        '''

        return f'({self.x} , {self.y})'

    def __add__(self, other):

        '''
        Retorna um vetor que é a soma dos dois vetores
        A soma de dois vetores é
        v1 v2 = v1.x + v2.x, v1.y + v2.y
        '''
        
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def move(self, other):

        '''
        Movimenta o vector tomando como refer}encia o parâmetro other.
        A nova coordenada x será o valor atual somando com a coordenada x de other.
        Mesma forma para a coordenada y. 
        '''

        self.x = self.x + other.x
        self.y = self.y + other.y

        
