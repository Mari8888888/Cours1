digitlist = ['0','1','2','3','4','5','6','7','8','9']
strnumber = ''
count = ''
numberlist = []
s = ''
strletter = ''
with open('dataset_3363_2.txt') as inf:
    for line in inf:
        line = line.strip()
        for i in range(1, len(line)): #заполняем новую строку числами через пробел
            if line[i] in digitlist:
                strnumber += line[i]
            else:
                strnumber += ' '
        for i in range(len(strnumber)): #делаем из строки с числами список с числами
            if strnumber[i] != ' ':
                count += strnumber[i]
                if i == len(strnumber) - 1:
                    numberlist += [count]
            else:
                numberlist += [count]
                count = ''
        for i in range(0, len(line)):  #записываем отдельную строку с буквами
            if line[i] not in digitlist:
                strletter += line[i]
        for i in range(0, len(strletter)):
            s += str(strletter[i]) * int(numberlist[i])
with open('dataset_3363_2.txt', 'w') as ouf:
    ouf.write(s)








