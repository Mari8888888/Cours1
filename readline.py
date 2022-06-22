import requests as requests
with open('dataset_3378_2.txt') as inf0:
    url = inf0.readline().strip()
r = requests.get(url)
inf = r.text
for line in inf:
    line = line.strip()
inf = inf.splitlines()
print(len(inf))