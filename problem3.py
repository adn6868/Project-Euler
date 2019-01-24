'''Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def sol1():
	num = 600851475143
	i = 2
	primes = []
	while i <= num:
		if i not in primes and num % i == 0:
			primes.append(i)
			num = num / i

		i+=1

	return max(primes)

if __name__ == '__main__':
	print(sol1())