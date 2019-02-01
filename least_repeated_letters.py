# your code goes here
ans=list(map(str,input().split()))
n=""
for i in ans:
	n+=i
c=0
for i in n:
	if n.count(i)==1:
		print(i,end=" "	)
