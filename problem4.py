'''
Problem 4
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def sol1():
	i = 999
	j = 999
	ans = {}
	for i in range(100,1000):
		for j in range(100,1000):
			cur = i*j
			if str(cur) == str(cur)[::-1]:
				ans[cur] = (i,j)
	print(ans[906609])
	return max(ans.keys())
if __name__ == '__main__':
	print(sol1())
