def is_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    return prime

for n in range(3,1000):
    if is_prime(n):
        print(n)
