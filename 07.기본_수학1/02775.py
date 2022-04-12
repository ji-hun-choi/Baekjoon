import math

t = int(input())

for i in range(t):
	k = int(input())
	n = int(input())
	c = math.comb(n+k,n-1)
	print(c)