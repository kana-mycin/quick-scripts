"""
Don't remember what this was exactly but it was probably a CS70 problem.
"""

def factorial (n):
	if n==0:
		return 1	
	return n*factorial(n-1)

def choose(n,k):
	return factorial(n)/(factorial(n-k)*factorial(k))

def win_chance(win_rate, games):
	sum=0
	for x in range (games-1, 2*games-1):
		i=x-games+1
		print("x=", x, ", i=", i)
		sum += (choose(x, i))*(pow((1-win_rate),i))
	while games > 0:
		sum=sum*win_rate
		games-=1
	return sum

#win probability
p = 51/100

#game req to win
g = 100
print(p)
print(win_chance(p, g))

