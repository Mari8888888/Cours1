lst = [int(i) for i in input().split()]
x = int(input())
l = len(lst)
s = ''
for i in range(0, l):
  if lst[i] == x:
    s += str(i) + ' '
if len(s) == 0:
  print("Отсутствует")
else:
  print(s)

