table_class = []
grows_dict = {e: 0 for e in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}
class_dict = {e: 0 for e in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}
with open('dataset_3380_5.txt') as inf:
    for line in inf:
        line = line.strip().split('\t')
        table_class += [line]
for i in range(len(table_class)):
    grows_dict[int(table_class[i][0])] += int(table_class[i][2])
    class_dict[int(table_class[i][0])] += 1
for key in grows_dict:
    if grows_dict[key] == 0:
        grows_dict[key] = '-'
    else:
        grows_dict[key] = grows_dict[key]/class_dict[key]
with open('grows.txt', 'w') as ouf:
    for key, value in grows_dict.items():
        s = str(key) + ' ' + str(value) + '\n'
        ouf.write(s)

