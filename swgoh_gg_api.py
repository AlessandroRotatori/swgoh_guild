# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:39:13 2018

@author: alessandro.rotatori
"""

import requests

url_new = 'https://swgoh.gg/api/characters'

r = requests.request('GET', url_new)

toon_list = loads(r.content.decode('utf-8'))