wordset = set()
wordlist = []
valuelist = []
word = ''
key = 0
d = {}
dict = {}
with open('dataset_3363_3.txt') as inf:
    for line in inf:
        line = line.strip().lower()
        for i in range(len(line)):
            if line[i] != ' ':
                word += line[i]
                if i == len(line) - 1:
                    wordset.add(word)
                    wordlist += [word]
            else:
                wordset.add(word)
                wordlist += [word]
                word = ''
for c in wordset:
    for k in wordlist:
        if c == k:
            key += 1
    d[c] = key
    valuelist += [key]
    key = 0
maxnumber = max(valuelist)
valuelist = []
for key, value in d.items():
    if value >= maxnumber:
       dict [key] = value
minletter = min(dict)
str = str(minletter) + ' ' + str(dict[minletter])
with open('dataset_3363_3.txt', 'w') as ouf:
     ouf.write(str)








