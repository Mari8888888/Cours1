str = 'abc a bCd bC AbC BC BCD bcd ABC'
str = str.lower()
wordset = set()
wordlist = []
valuelist = []
word = ''
key = 0
d = {}
dict = {}
for i in range(len(str)):
    if str[i] != ' ':
        word += str[i]
        if i == len(str) - 1:
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
maxletter = 'a'
for key in dict:
    if key > maxletter:
        maxletter = key
print(dict)
