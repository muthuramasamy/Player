# your code goes here
s,k=map(str,input().split())
a=s.lower()
b=k.lower()
c=0
if len(a)==len(b):
	for i in range(len(a)):
		if a[i]!=b[i]:
			c=c+1
	if c==0:
		print("yes")
	else:
		print("no")
else:
	print("no")
