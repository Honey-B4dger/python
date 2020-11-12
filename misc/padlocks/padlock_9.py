def is_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    return prime

primes = []

for n in range(2,1000):
    if is_prime(n):
        primes.append(n)

print(primes)

print(round(sum(primes)/len(primes), 0))
