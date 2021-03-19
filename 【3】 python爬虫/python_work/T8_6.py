def city_country(city,country):
	str=city.title() +' , '+ country.title()
	return str

while True:
	print("Entry a 'q' to exit.")
	city=input("Please input city:")
	if city=='q':
		break
	print("Entry a 'q' to exit.")
	country=input("Please input country:")
	if country=='q':
		break
	
	res=city_country(city,country)
	print(res+"\n")
	
