import requests
from pprint import pprint

class hero():
    def __init__(self, name):
        self.name = name
        self.url_link = 'https://superheroapi.com/api/2619421814940190/search/' + name
        resp = requests.get(self.url_link).json()
        self.intelligence = int(resp["results"][0]['powerstats']['intelligence'])

if __name__ == '__main__':
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    hero_class_list = []
    hero_int_dikt = {}

    for x in hero_list:
        hero_i = hero(x)
        hero_class_list += [hero_i]

    for x in hero_class_list:
        hero_int_dikt[x.name] = x.intelligence
    print(max(hero_int_dikt, key=hero_int_dikt.get))
