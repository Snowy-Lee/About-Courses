'''import T8_16module_name

unprinted_models = ['car','train','subway']
completed_models = []

T8_16module_name.move_models(unprinted_models[:],completed_models)
print(completed_models)'''

'''from T8_16module_name import move_models

unprinted_models = ['car','train','subway']
completed_models = []

move_models(unprinted_models[:],completed_models)
print(completed_models)'''

'''from T8_16module_name import move_models as fn

unprinted_models = ['car','train','subway']
completed_models = []

fn(unprinted_models[:],completed_models)
print(completed_models)'''

'''import T8_16module_name as mn

unprinted_models = ['car','train','subway']
completed_models = []

mn.move_models(unprinted_models[:],completed_models)
print(completed_models)'''

from T8_16module_name import *

unprinted_models = ['car','train','subway']
completed_models = []

move_models(unprinted_models[:],completed_models)
print(completed_models)
