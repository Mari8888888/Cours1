a = [int(i) for i in input().split()]
l = len(a)
b = ''
sum = 0
if l == 1:
    b += str(a[0])
else:
    for i in range(0, l):
        if i == l - 1:
            sum = a[i - 1] + a[0]
            b += str(sum) + ' '
            sum = 0
        elif i == 0:
            sum = a[i + 1] + a[-1]
            b += str(sum) + ' '
            sum = 0
        else:
            sum = a[i - 1] + a[i + 1]
            b += str(sum) + ' '
            sum = 0
print(b)
