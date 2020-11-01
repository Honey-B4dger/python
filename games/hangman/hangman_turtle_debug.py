import turtle 

width = 800
height = 600

class hangman(turtle.Turtle):
#    def __init__(self, scale):
#        self.scale = scale
    self.scale = 100
    def get_scale(self):
        return self.scale

    def torso(self):
        print('foo')
        self.penup()
        self.goto(0,0)
        self.setheading(90)
        self.pendown()
        self.forward(self.scale)
        self.penup()
        self.goto(0,0)

s = turtle.Screen()
s.setup(width, height)
s.title('superTurtle')

h = hangman()
print(type(h))
print(f'Scale ist : {h.get_scale()}')
h.torso()
#h.legs()
#h.arms()
#h.head()

#wort = input('Bitte nenne das Wort, welches erraten werden soll: ')
#
#wort = wort.upper()
#
#print(wort)
#toby.square(100)
turtle.done()
