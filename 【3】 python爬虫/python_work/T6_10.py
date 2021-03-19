numbers={'Lisa':[2,5,1],
		'Mike':[3,6,8],
		'Jack':[3,8],
		'Sara':[4,0,3],
		}
		
for k,v in numbers.items():
	print(k.title() + "'s favorite numbers are ")
	for value in v:
		print("\t" + str(value))
