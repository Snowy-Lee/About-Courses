def build_profile(first,last,**users):
	profile={}
	profile['first']=first
	profile['last']=last
	for key,value in users.items():
		profile[key]=value
	return profile
		
user=build_profile('Li','Xue',location='TianMen',school='WuHan',age=22)
print(user)
