# your code goes here
s=input()
count = [0 for i in range(26)]
for c in s:
    if c.isalpha(): count[ord(c.lower()) - 97] += 1
print(max(count))
