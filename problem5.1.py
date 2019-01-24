'''
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

'''

def sol1(num):

	i = 2
	primes = {}
	while i <= num:
		if num % i == 0:
			if i in primes.keys():
				primes[i] +=1
				num = num / i	
				i = 2		
			else:
				primes[i] = 1
				num = num / i
				i = 2 
		i+=1

	return primes

if __name__ == '__main__':
	for i in range(1,20):
		print(sol1(i))