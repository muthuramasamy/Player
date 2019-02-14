# your code goes here
def permutation(lst):
	if len(lst)==0:
		return []
	if len(lst)==1:
		return[lst]
	k=[]
	for i in range(len(lst)):
		m=lst[i]
		remlst=lst[:i]+lst[i+1:]
		for r in permutation(remlst):
			k.append([m]+r)
	return k
		
n=list(input())
for i in permutation(n):
	for d in i:
		print(d,end="")
	print()
