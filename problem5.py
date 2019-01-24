'''
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

'''
import concurrent.futures
import threading



# primes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def sol1(start):
	# print("yo")
	ans = start 
	go = True
	while ans < start+10000:
		if good(ans):
			print("found it"+ str(ans))
			return ans
		else:
			ans+=1
	print('range {0} to {1} completed \n'.format(start,start+10000))
	return 0


def good (ans):
	# primes = [8,11,12,13,14,15,16,17,18,19,20]
	# primes = [10,9,8,7,6,3,2,1]
	primes = [20,19,18,17,16,15,14,13,12,11,8]
	for i in primes:
		if ans % i != 0:
			return False
	return True

if __name__ == '__main__':
	# print(sol1())
	alist = list(range(1,100000000,10000))
	LOCAL_THREAD = threading.local()
	with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
		executor.map(sol1,alist)