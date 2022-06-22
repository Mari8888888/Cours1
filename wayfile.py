import requests as requests
catalog = 'https://stepic.org/media/attachments/course67/3.6.3/'
with open('dataset_3378_3.txt') as inf0:
    url_in_file = inf0.readline().strip()
def url(name):
    if "We" in requests.get(name).text.split(' '):
        return requests.get(name).text
    else:
        return url(catalog + requests.get(name).text)
print(url(url_in_file))

