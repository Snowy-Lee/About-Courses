users=['admin','Amy','Mike','Jack','Rose']
for user in users:
	if user=='admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello "+ user+", thank you for logging in again")

del users[:]
if user:
	print("We need to find some users!")
