# your code goes here
n,k=map(int,input().split())
li=list(map(int,input().split()))
f=0
for i in li:
	if i==k:
		f=1
	else:
		continue
if f==1:
	print("Yes")
else:
	print("No")
