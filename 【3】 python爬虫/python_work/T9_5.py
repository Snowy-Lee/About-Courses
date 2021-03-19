class User():
	def __init__(self,first_name,last_name,sex,age):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.age = age
		self.login_attempts = 0
		
	def describe_user(self):
		print("Your name is " + self.first_name.title() + self.last_name.title() +".")
		print("Your sex is " + self.sex + " and age is " +str(self.age) + ".")
	
	def greet_user(self):
		print("Hello," + self.first_name.title() + self.last_name.title() +"!")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
	def read_login_attempts(self):
		print("The login_attempts are " + str(self.login_attempts) + ".")
		
user_one =User("li","xue","woman",18)
user_one.describe_user()
user_one.greet_user()

user_one.increment_login_attempts()
user_one.read_login_attempts()

user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.read_login_attempts()

user_one.reset_login_attempts()
user_one.read_login_attempts()

