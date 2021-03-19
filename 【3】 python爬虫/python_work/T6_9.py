favorite_places={'lisa':['Lasa','ChongQing','Xian'],
				'Mary':['Daocheng','Changsha'],
				'Jack':['Wuhan','Zhejiang'],
				}

for k,v in favorite_places.items():
	print(k.title() + "'s favorite places are ")
	for value in v:
		print("\t" + value.title())
