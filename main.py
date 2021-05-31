import json
import os
import hashlib

with open(os.path.join(os.getcwd(), 'countries.json'))as json_file:
    data = json.load(json_file)
WIKI_MAIN = 'https://en.wikipedia.org/wiki/'


class WikiIterator:

    def __init__(self):
        self.d = {}

    def __iter__(self):
        self.a = iter(data)
        return self

    def __next__(self):
        x = next(self.a)
        self.d[x['name']['common']] = (WIKI_MAIN + x['name']['common']).replace(' ', '_')
        return self.d


def generator():
    with open(os.path.join(os.getcwd(), 'countries_new.json'))as json_file:
        data3 = json.load(json_file)
    for key, val in data3.items():
        yield hashlib.md5((key+val).encode()).hexdigest()


if __name__ == '__main__':
    for country_link in WikiIterator():
        with open(os.path.join(os.getcwd(), 'countries_new.json'), 'w', encoding="utf-8") as f:
            data2 = json.dump(country_link, f)
    for hash_ in generator():
        print(hash_)
