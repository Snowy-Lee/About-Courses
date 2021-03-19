def move_models(unprinted_models,completed_models):
	while unprinted_models:
		current_model = unprinted_models.pop()
		print("正在打印" + current_model)
		completed_models.append(current_model)
