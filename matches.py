n = int(input())
table = []
teamset = set()
for i in range(n):
    row = [j for j in input().split(';')]
    table += [row]
for i in range(n):
    for j in range(0, 4, 2):
        teamset.add(table[i][j])
table_results = {e: [0, 0, 0, 0, 0] for e in teamset}
for i in range(n):
    if table[i][0] in teamset:
        table_results[table[i][0]][0] += 1
    if table[i][2] in teamset:
        table_results[table[i][2]][0] += 1
    if int(table[i][1]) > int(table[i][3]):
        table_results[table[i][0]][1] += 1
        table_results[table[i][2]][3] += 1
    elif int(table[i][1]) < int(table[i][3]):
        table_results[table[i][2]][1] += 1
        table_results[table[i][0]][3] += 1
    else:
        table_results[table[i][0]][2] += 1
        table_results[table[i][2]][2] += 1
for value in table_results.values():
    value[4] = value[1] * 3 + value[2] * 1
for key, value in table_results.items():
    print(key + ': ', *value, end='\n')