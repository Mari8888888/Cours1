n = int(input())
way_dict = {'восток': 0, 'север': 0, 'запад': 0, 'юг': 0}
for i in range(n):
    row = [i for i in input().split()]
    way_dict[row[0]] += int(row[1])
way_dict['север'] -= way_dict['юг']
way_dict['восток'] -= way_dict['запад']
print(way_dict['восток'], way_dict['север'])
