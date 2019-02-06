#guvi
m,n = map(int,input().split())
num=n
i=0
while num<=m:
	if num==m:
		print("yes")
		break
	num=n**i
	i+=1
else:
	print("no")
