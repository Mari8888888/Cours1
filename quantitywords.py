l = [i.lower() for i in input().split()]
s = set()
k = []
count = 0
for i in range(len(l)):
  s.add(l[i])
for c in l:
  if c in s and c not in k:
    k += [c]
for c in k:
  for n in l:
    if c == n:
      count += 1
  print(c, count)
  count = 0