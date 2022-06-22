d = int(input())
wordset = set()
textlist = []
for i in range(d):
    s = input().lower()
    wordset.add(s)
l = int(input())
for i in range(l):
    list = [i for i in input().lower().split()]
    for j in range(len(list)):
        if list[j] not in textlist:
            textlist += [list[j]]
for i in range(len(textlist)):
    if textlist[i] not in wordset:
        print(textlist[i])