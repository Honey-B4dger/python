import turtle 

width = 800
height = 600

class hangman(turtle.Turtle):

    fails = 0

    def __init__(self, scale):
        super().__init__()
        self.scale = scale

    def get_scale(self):
        return self.scale

    def torso(self):
        print('foo')
        self.penup()
        self.goto(0,0)
        self.setheading(90)
        self.pendown()
        self.forward(self.scale)

    def hill(self):
        self.penup()
        self.goto(-self.scale, -self.scale / 2)
        self.setheading(90)
        self.pendown()
        self.circle(self.scale / 2, 180)

    def pylon(self):
        self.penup()
        self.goto(-1.5 * self.scale, 0)
        self.setheading(90)
        self.pendown()
        self.forward(2 * self.scale)

    def beam(self):
        self.penup()
        self.goto(-1.5 * self.scale, 2 * self.scale)
        self.setheading(0)
        self.pendown()
        self.forward(1.5 * self.scale)

    def legs(self):

        for angle in [225, 315]:
            self.penup()
            self.goto(0,0)
            self.setheading(angle)
            self.pendown()
            self.forward(0.25 * self.scale)

    def arms(self):

        for angle in [45, 135]:
            self.penup()
            self.goto(0,0.55 * self.scale)
            self.setheading(angle)
            self.pendown()
            self.forward(0.25 * self.scale)

    def head(self):

        self.penup()
        self.goto(0,self.scale)
        self.setheading(0)
        self.pendown()
        self.circle(0.2 * self.scale)


s = turtle.Screen()
s.setup(width, height)
s.title('superTurtle')

h = hangman(100)
h.width(2)
h.hideturtle()
#print(f'Scale ist : {h.get_scale()}')
h.hill()
h.pylon()
h.beam()
h.torso()
h.legs()
h.arms()
h.head()

#wort = input('Bitte nenne das Wort, welches erraten werden soll: ')
#
#wort = wort.upper()
#
#print(wort)
#toby.square(100)
turtle.done()
