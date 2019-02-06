#guvi
n=int(input())
f=0
for i in range(1,n+1,2):
	if n%i==0:
		if f==0:
			print(i,end="")
			f+=1
		else:
			print("",i,end="")
	
