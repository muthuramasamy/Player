# your code goes here
n=input()
a=['a','e','i','o','u','A','E','I','O','U']
l=[]
l1=[]
for i in n:
	if i in a:
		l.append(i)
	else:
		l1.append(i)
c=l+l1
for i in range(len(c)):
	if i==len(c)-1:
		print(c[i],end='')
	else:
		print(c[i],end='')
