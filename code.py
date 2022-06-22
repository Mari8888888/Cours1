s1, s2 = input(), input()
s1list = []
s2list = []
s1list += s1
s2list += s2
str_code = ''
str_decode = ''
code = {e: '' for e in s1list}
decode = {e: '' for e in s2list}
for i in range(len(s1)):
    code[s1[i]] = s2[i]
    decode[s2[i]] = s1[i]
s3, s4 = input(), input()
for i in range(len(s3)):
    for key in code:
        if s3[i] == key:
            str_code += code[key]
for i in range(len(s4)):
    for key in decode:
        if s4[i] == key:
            str_decode += decode[key]
print(str_code, end='\n')
print(str_decode, end='\n')

