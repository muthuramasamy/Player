n=int(input(""))
s=input()
s1=""
a=['a','e','i','o','u','A','E','I','O','U']
for i in reversed(s):
	if i not in a:
		s1+=i
print(s1)
