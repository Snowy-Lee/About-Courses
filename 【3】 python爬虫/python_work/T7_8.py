sandwich_orders=['sala','bifu','chicken']
finished_sandwiches=[]

while sandwich_orders:
	temp=sandwich_orders.pop()
	print("I made your " +temp +" sandwich")
	finished_sandwiches.append(temp)
	
print(finished_sandwiches)
