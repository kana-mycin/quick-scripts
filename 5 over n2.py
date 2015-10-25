n = 9
reps = 1000000
count = 0
from random import randint

for x in range(0,reps):
	die1 = randint(1,n)
	die2 = randint(1,n)
	if die1<4 and die2<4:
		if die1==3 or die2==3:
			count = count+1

print(count/reps)
