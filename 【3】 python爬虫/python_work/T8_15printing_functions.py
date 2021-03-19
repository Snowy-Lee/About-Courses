# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
def move_model(unprinted_designs,completed_models):
	while unprinted_designs: 
		current_design = unprinted_designs.pop() 
		 
		#模拟根据设计制作3D打印模型的过程
		print("Printing model: " + current_design) 
		completed_models.append(current_design) 
	
def show_model(completed_models):
	print("\nThe following models have been printed:") 
	for model in completed_models:
		print(model)
