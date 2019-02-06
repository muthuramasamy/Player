# your code goes here
a,b=map(str,input().split())
c=int(b)
n=len(a)
ans=a
for i in range(c):
	ans=ans[-1]+ans[:n-1]
print(ans)
