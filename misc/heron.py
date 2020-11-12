import math

def calculate_triangle_are():
    print('Bitte gib nacheinander die 3 Seitenlaengen an.')
    print('')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))


    perimeter = a + b + c
    s = perimeter /2

    area = math.sqrt(s * (s - a) * (s - b) * (s -c))

    print(f'The area is: {area}')


if __name__ == '__main__':
    calculate_triangle_are()
