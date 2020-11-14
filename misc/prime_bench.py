import time

max_range = 100000
interval = 1000
max_prime = 2

def is_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    return prime

if __name__ == '__main__':

    try:
        start = time.time()
        for n in range(2,max_range):
            if is_prime(n):
                max_prime = n
            if n% interval ==0:
                print(f'current max_prime: {max_prime}')
    except KeyboardInterrupt:
        pass
    finally:
        print('')
        print(f'maximum range: {max_range}')
        print(f'final max_prime: {max_prime}')
        print(f'elapsed time: {round(time.time() - start,1)} s')
