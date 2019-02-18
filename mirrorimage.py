# your code goes here
n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
l.reverse()
if l==m:
	print('yes')
else:
	print('no')
