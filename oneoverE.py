def summation(x,term):
	total,k=0,1
	while(k<=x):
		total,k=total+term(k),k+1
	return total

def eterm(x):
	return pow(-1,x-1)/factorial(x-1)

def factorial(x):
	if x==0:
		return 1
	total=1
	while x>0:
		total=total*x
		x-=1
	return total

def oneoverE(reps):
	return summation(reps,eterm)

testnum=20

print("First ", testnum, " approximations of 1/e: ")
i=1
while i<=20:
	print(oneoverE(i))
	i+=1