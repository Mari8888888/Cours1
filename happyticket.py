a = input()
b = "1" + a
s = int(b)
a = s % 10
s = s // 10
b = s % 10
s = s // 10
c = s % 10
s = s // 10
d = s % 10
s = s // 10
e = s % 10
s = s // 10
f = s % 10
if a + b + c == d + e + f:
 print ("Счастливый")
else:
 print ("Обычный")