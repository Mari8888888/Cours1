a = [int(i) for i in input().split()]
a.sort()
b = []
l = len(a)
r = ''
for i in range(0, l-1):
  if a[i+1] == a [i] and a[i] not in b:
    b += [a[i]]
for c in b:
  r += str(c) + ' '
print (r)