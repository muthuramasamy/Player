import collections
m,n = map(str,input("").split())
d = dict(collections.Counter(m))
print(d[n])
