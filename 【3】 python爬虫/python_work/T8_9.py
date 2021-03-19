def show_magicians(magicians):
	#打印魔术师列表
	for magic in magicians:
		print(magic.title())
		
def make_great(magicians):
	for i in range(0,3):
		magicians[i]='the Great ' + magicians[i]
		
def make_greater(copy):
	for i in range(0,3):
		copy[i]='the Great ' + copy[i]
	return copy

magicians=['liuqian','eric','amy']
show_magicians(magicians)

#make_great(magicians)
#show_magicians(magicians)

res=make_greater(magicians[:])
show_magicians(res)
show_magicians(magicians)
