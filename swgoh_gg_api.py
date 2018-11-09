# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:39:13 2018

@author: alessandro.rotatori
"""

import requests
import json

url_new = 'https://swgoh.gg/api/characters'

r = requests.request('GET', url_new)

toon_list = loads(r.content.decode('utf-8'))
name_list = [d['name'] for d in toon_list]
map_id_name = pd.DataFrame({'base_id': [d['base_id'] for d in toon_list],
                       'name': [d['name'] for d in toon_list]})

with open('general_character_list.json', 'w') as outfile:
        json.dump(map_id_name, outfile)
        
del toon_list, name_list
