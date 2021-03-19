from T9_10Restaurant import IceCreamStand

my_restaurant = IceCreamStand('drink','sweet food')
print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.read_flavors()