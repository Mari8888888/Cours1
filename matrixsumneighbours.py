a = []
for i in range(1000):
  row = [i for i in input().split()]
  if 'end' not in row:
    for i in range(len(row)):
      row[i] = int(row[i])
    a += [row]
    col = len(row)
  else:
    break
b = [[0 for j in range(col+2)] for i in range(len(a)+2)]
for i in range(0, len(a)+2):
  for j in range(0, col+2):
    if 0 < i < len(a)+1 and 0 < j < col+1:
      b[i][j] = a[i-1][j-1]
for i in range(0, len(a)+2):
  for j in range(0, col+2):
    if i == 0:
      b[i][j] = b[len(a)][j]
    if i == len(a) + 1:
      b[i][j] = b[1][j]
    if j == 0:
      b[i][j] = b[i][col]
    if j == col + 1 :
      b[i][j] = b[i][1]
a = [[0 for j in range(col+2)] for i in range(len(a)+2)]
for i in range(1, len(a) - 1):
  for j in range(1, col+1):
      a[i][j] = b[i-1][j] + b[i+1][j] + b[i][j-1] + b[i][j+1]
      print(a[i][j], end=' ')
  print()
