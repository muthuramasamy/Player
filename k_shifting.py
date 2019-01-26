n,k = map(int,input().split())
l = list(map(int,input().split()))
if(n<k):
    for i in range(n):
        if(i == n-1):
            print(l[i],end="")
        else:
            print(l[i],end=" ")
else:
    a= n-k
    for i in range(a,n):
        print(l[i],end = " ")
    for i in range(0,a):
        if(i==a-1):
            print(l[i],end="")
        else:
            print(l[i],end = " ")
