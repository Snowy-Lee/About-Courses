cities={'Beijing':{'country':'China',
				   'population':'150millon',
				   'fact':'it is shoudu',
				   },
				   
		'Xian':{'country':'China',
				'population':'100millon',
				'fact':'it has many snacks',
				},
				
		'Chengdu':{'country':'China',
				'population':'80millon',
				'fact':'it has pandas',
				},
		}
		
for k,v in cities.items():
	print(k.title())
	print("\tIt belongs to " + v['country'] +".")
	print("\tIt has " + v['population'] +" population.")
	print("\t" + v['fact'] + "\n")
