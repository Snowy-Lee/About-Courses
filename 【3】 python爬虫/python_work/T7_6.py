mes="\ninput your age "
mes +="\nEnter quit when you finished."

age = input(mes)
while age !='quit':
		age=int(age)
		if age>0 and age<3:
			print("Free")
		elif age <= 12:
			print("10 dollors")
		else:
			print("15 dollors")
		age = input(mes)
