#hey guvi
a,b=map(str,input().split())
for i in a:
	if i in b:
		print('yes')
		break
else:
	print('no')
