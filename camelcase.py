a=input("")
b=""
for i in range(len(a)):
	if i==0:
		b+=a[i].upper()
	elif (a[i-1].isspace()):
		b+=a[i].upper()
	else:
		b+=a[i]
print(b)
	
