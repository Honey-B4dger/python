class Quadruped():
    snouts = 1
    def __init__(self, name):
        self.name = name
        self.legs = 4

class Dog(Quadruped):
    def make_noise(self):
        print('woof')

if __name__ == '__main__':

    wuffi = Dog('wuffi')
    print(dir(Quadruped))
    print(dir(Dog))
    print(dir(wuffi))
    #bello = Dog('bello')
    #print(wuffi.name)
    #print(type(wuffi))
    #print(wuffi.legs)
    #wuffi.make_noise()
    #print(wuffi.snouts)
    #wuffi.snouts = 2
    #Quadruped.snouts += 1
    #print(wuffi.snouts)
    #print(bello.snouts)
