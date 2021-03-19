def make_album(singer,album,count=''):
	person={'singer':singer,'album':album}
	if count:
		person['count']=count
	return person

while True:
	print("Entry a 'q' to exit.")
	singer=input("Please input singer:")
	if singer=='q':
		break
	print("Entry a 'q' to exit.")
	album=input("Please input album:")
	if album=='q':
		break
	
	res=make_album(singer,album)
	print(res)
