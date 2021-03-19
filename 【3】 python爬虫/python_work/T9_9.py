class Car():
	'''模拟普通汽车'''
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("you can't roll back an odometer!")
			
	def increment_odometer(self,miles):
		self.odometer_reading +=miles
		
class Battery():
	'''电瓶'''
	def __init__(self,battery_size=70):
		self.battery_size = battery_size
		
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-KWH battery.")
		
	def get_range(self):
	#续航里程
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += "miles on a full charge."
		print(message)
		
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
	
class ElectricCar(Car):
	'''电动车'''
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()
		
my_car = ElectricCar('BMW','model s',2020)
print(my_car.get_descriptive_name())
#里程默认为0
my_car.read_odometer()

#更新里程
my_car.update_odometer(50)
my_car.read_odometer()

#电瓶容量，初始为70
my_car.battery.describe_battery()
#根据容量判断里程
my_car.battery.get_range()

#统一升级成85
my_car.battery.upgrade_battery()
#里程增加
my_car.battery.get_range()
	
