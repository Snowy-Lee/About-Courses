current_users=['Lisa','Amy','Mike','Jack','Rose']
new_users=['MisWang','John','Sara','Mike','AMY']
lower_users=[]
for current_user in current_users:
	lower_users.append(current_user.lower())
for user in new_users:
	if user.lower() in lower_users:
		print(user+",please change a name.")
	else:
		print(user+" is not used.")
