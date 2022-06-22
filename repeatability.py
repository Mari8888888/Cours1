n = int(input())
a = []
b = []
s = ''
for i in range(1, n + 1):
  a += [i]
for k in a:
  b += [k]*k
for i in range(0, n):
  s += str(b[i]) + ' '
print(s)