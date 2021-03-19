pet1={'type':'dog',
	  'owner':'lisa'
	 }
	
pet2={'type':'cat',
	  'owner':'mike'
	 }
	 
pet3={'type':'mouse',
	  'owner':'amy'
	 }
	 
pets=[pet1,pet2,pet3]

for pet in pets:
	print("Type is " + pet['type'].title() +".")
	print("Owner is " + pet['owner'].title() +".\n")
