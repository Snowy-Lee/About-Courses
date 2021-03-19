sandwich_orders=['sala','pastrami','bifu','pastrami','pastrami','chicken']
finished_sandwiches=[]

print("pastrami is sold out.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	temp=sandwich_orders.pop()
	print("I made your " +temp +" sandwich")
	finished_sandwiches.append(temp)
	
print(finished_sandwiches)
	
