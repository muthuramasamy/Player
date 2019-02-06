# your code goes here
n=int(input())
if(n>= -2147483648 and n<= 2147483647):
    print("INT")
elif(n>=9223372036854775808 and n<= 9223372036854775807):
    print("LONG LONG")
else:
    print("LONG")
