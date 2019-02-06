# your code goes here
n=input()
k=int(n.replace("," , ""))
if k>= -2147483648 and k<= 2147483647:
    print("INT")
elif k>=9223372036854775808 and k<= 9223372036854775807:
    print("LONG LONG")
else:
    print("LONG")
