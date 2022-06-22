s = input()
l = len(s)
sum = 1
s2 = ''
if l == 1:
    print(s + '1')
else:
    for i in range(0, l - 1):
        if s[i + 1] == s[i]:
            sum += 1
            if i == l - 2:
                s2 = s2 + s[i] + str(sum)
        else:
            if i == l - 2:
                s2 = s2 + s[i] + str(sum) + s[i + 1] + "1"
            else:
                s2 = s2 + s[i] + str(sum)
                sum = 1
print(s2)
