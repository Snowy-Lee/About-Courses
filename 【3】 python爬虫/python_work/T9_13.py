from collections import OrderedDict

python_words =  OrderedDict()
python_words['Array'] = 'consist of a collection of elements identified by index or key'
python_words['Pointer'] = 'point to another value in the computer memory using its memory address'
python_words['Class'] = 'data structure with data and functions as its members'
python_words['Traversal'] = 'visit each element in some order'
python_words['Recursion'] = 'repeate items in a self-similar way'

for key,value in python_words.items():
	print(key + ": " + value + "\n")