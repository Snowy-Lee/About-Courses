favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 } 
friends = ['phil', 'sarah','jack','mara'] 
for name in friends:  
	if name in favorite_languages.keys(): 
		print(name.title() + ", thank you!")
		
	if name not in favorite_languages.keys(): 
		print(name.title() + ", please join us!")
