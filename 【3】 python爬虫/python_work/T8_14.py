def build_car(factory,model,**car_info):
	car={}
	car['factory']=factory
	car['model']=model
	for key,value in car_info.items():
		car[key]=value
	return car
	
car=build_car("Dongfeng","X-11",blue='pink',package='music')
print(car)
