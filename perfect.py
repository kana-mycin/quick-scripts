def perfects(num_cap=10000):

	i=1
	perf_list=[]
	while i <= num_cap:
		if sum(get_factors(i)) == i:
			perf_list+=[i]
		i+=1
	return perf_list

def get_factors(i):
	return [x for x in range(1, i//2+1) if i%x==0]

print(perfects())