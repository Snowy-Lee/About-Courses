mes="\ninput your age "
mes +="\nEnter quit when you finished."

while True:
	age = input(mes)
	if age == 'quit':
		break
	else:
		age=int(age)
		if age>0 and age<3:
			print("Free")
		elif age <= 12:
			print("10 dollors")
		else:
			print("15 dollors")
