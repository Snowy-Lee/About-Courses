def make_album(singer,album,count=''):
	person={'singer':singer,'album':album}
	if count:
		person['count']=count
	return person
	
res=make_album('zhangjie','angel',25)
print(res)
