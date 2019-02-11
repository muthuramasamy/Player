# your code goes here
s,k=map(str,input().split())
c=0
if len(s)==len(k):
	for i in range(len(s)):
		if s[i]!=k[i]:
			c=c+1
	if c==0:
		print("yes")
	else:
		print("no")
else:
	print("no")
