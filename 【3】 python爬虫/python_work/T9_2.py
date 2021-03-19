class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print("The restaurant name is " + self.restaurant_name.title() +".")
		print("The cuisine type is " + self.cuisine_type.title() + ".")
		
	def open_restaurant(self):
		print("The restaurant is opening.\n")

restaurant_one = Restaurant('vegetables','Italian food')
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

restaurant_two = Restaurant('noodles','Amercian food')
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three = Restaurant('sandwichs','Japanees food')
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
