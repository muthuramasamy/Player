# your code goes here
p,a=map(int,input().split())
total=p//2
for i in range(total,0,-1):
	for j in range(1,total):
		if i+j==total and i*j==a:
			print("yes")
			exit(0)
else:
	print("no")
