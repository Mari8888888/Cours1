k = n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
r, f, col2, l, t, s, col1, row2, h, p, row1 = 0, 0, 0, -1, n - 1, n - 1, n - 1, n - 1, n - 1, 1, 1
for i in range(0, n):
  for j in range(0, n):
    if i == 0:
      a[i][j] = j + 1
while n >= n/2:
  for i in range(p, n):
    j = col1
    a[i][j] = a[i-1][j] + 1
  t -= 1
  col1 -= 1
  n -= 1
  for j in range(t,l,-1):
    i = row2
    a[i][j] = a[i][j+1] + 1
  row2 -= 1
  l += 1
  s -= 1
  for i in range(s, r, -1):
    j = col2
    a[i][j] = a[i+1][j] + 1
  r += 1
  col2 += 1
  f += 1
  for j in range(f,h):
    i = row1
    a[i][j] = a[i][j-1] + 1
  row1 += 1
  h -= 1
  p += 1
for i in range(k):
  for j in range(k):
    print(a[i][j], end=' ')
  print()