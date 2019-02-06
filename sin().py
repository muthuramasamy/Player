#guvi
import math
n=int(input())
rad=n*(math.pi)/180
if rad<1 and rad>0:
	print(round(math.sin(rad),2))
else:
	print(round(math.sin(rad)))
