class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print("The restaurant name is " + self.restaurant_name.title() +".")
		print("The cuisine type is " + self.cuisine_type.title() + ".")
		
	def open_restaurant(self):
		print("The restaurant is opening.")
		
	def set_number_served(self,number):
		self.number_served = number
		
	def increment_number_served(self,add_people):
		if add_people >= 0:
			self.number_served += add_people
		else:
			print("You can't decrese number.")
		
	def read_number(self):
		print("There had " + str(self.number_served) +" people eating here.")
		
		
my_restaurant = Restaurant('Chicken','Chinese food')
print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print("There had " + str(my_restaurant.number_served) +" people eating here.")
my_restaurant.number_served = 23
my_restaurant.read_number()

my_restaurant.set_number_served(40)
my_restaurant.read_number()

my_restaurant.increment_number_served(10)
my_restaurant.read_number()
