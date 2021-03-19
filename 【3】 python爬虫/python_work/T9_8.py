class User():
	def __init__(self,first_name,last_name,sex,age):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.age = age
		
	def describe_user(self):
		print("Your name is " + self.first_name.title() + self.last_name.title() +".")
		print("Your sex is " + self.sex + " and age is " +str(self.age) + ".")
	
	def greet_user(self):
		print("Hello," + self.first_name.title() + self.last_name.title() +"!")
		
class Privileges():
	def __init__(self):
		self.privileges = ["can add post","can delete post","can ban user"]
		
	def show_privileges(self):
		print(self.privileges)
		
class Admin(User):
	def __init__(self,first_name,last_name,sex,age):
		super().__init__(first_name,last_name,sex,age)
		self.privileges = Privileges()
		
admin =Admin("li","xue","woman",18)
admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()

