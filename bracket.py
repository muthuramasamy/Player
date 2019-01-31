# your code goes here
n=input()
c=0
d=0
for i in n:
	if i=="(":
		c=c+1
	elif i==")":
		d=d+1
if c==d:
	print('yes')
else:
	print('no')
