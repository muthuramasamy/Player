# your code goes 
#guvi
n=int(input())
l2=[]
for i in range(1,n+1):
	if n%i==0:
		l2.append(i)
	else:
		continue
for i in range(len(l2)):
	if i==len(l2)-1:
		print(l2[i],end="")
	else:
		print(l2[i],end=" ")
	
