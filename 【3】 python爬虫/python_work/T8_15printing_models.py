import T8_15printing_functions as pf

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = [] 

pf.move_model(unprinted_designs[:],completed_models)
pf.show_model(completed_models)

print(unprinted_designs)
