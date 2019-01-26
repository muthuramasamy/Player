# your code goes here
a=input("")
b=""
for i in range(0,len(a)-1,2):
	b=b+a[i+1]
	b=b+a[i]
print(b)
