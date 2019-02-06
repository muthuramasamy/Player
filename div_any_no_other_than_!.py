# your code goes here
n=int(input())
f=0
for i in range(2,n):
	if n%i==0:
		f=1
	else:
		continue
if f==1:
	print("yes")
else:
	print("no")
