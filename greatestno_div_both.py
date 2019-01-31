# your code goes here
n,k=map(int,input().split())
l2=[]
for i in range(1,k):
	if n%i==0 and k%i==0:
		l2.append(i)
print(max(l2))
