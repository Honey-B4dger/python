import os

hello = 'hello'
world = 'world'

def my_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print('Hello world!')
    if kwargs['verbose'] == True:
        print('Hello again!')


def hello_world():
    print(hello, world)

def cruel_world():
    #global world
    print(world)
    world = 'cruel world'

#my_func('spam', 'eggs', verbose = False)
os.system('clear')
hello_world()
cruel_world()
hello_world()

