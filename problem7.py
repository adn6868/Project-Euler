'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
def nthPrime (N):
    primes = []
    i = 2
    while len(primes) < N:
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        i+=1
        # print(primes)
    return primes[-1] 
if __name__ == "__main__":
    print(nthPrime(10001))