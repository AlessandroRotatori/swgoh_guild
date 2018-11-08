# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:20:55 2018

@author: alessandro.rotatori
"""
import requests
import pandas as pd
from json import loads, dumps, dump
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())

username = 'ObiAle'
password = 'alex87rot'
client_id = '123'
client_secret = 'abc'
urlBase = 'https://api.swgoh.help'
signin = '/auth/signin'
data_type = {'guild':'/swgoh/guild/',
             'player':'/swgoh/player/',
             'data':'/swgoh/data/'}
#general variables
data_types = ['guild','player','data']
all_criteria = ['events','units','arena','gear','mod-sets','mod-stats','skills','skill-types','tb','zetas','zeta-abilities','zeta-recommendations','battles']
allycode = 163532549

#definition
user = "username="+username     
user += "&password="+password
user += "&grant_type=password"
user += "&client_id="+client_id
user += "&client_secret="+client_secret

#Auth tests
sign_url = urlBase+signin
payload = user
head = {"Content-type": "application/x-www-form-urlencoded",
        'Content-Length': str(len(payload))}
r = requests.request('POST',sign_url, headers=head, data=payload, timeout = 10)
if r.status_code != 200:
    error = 'Cannot login with these credentials'
_tok = loads(r.content.decode('utf-8'))['access_token']

#player data
head = {'Method': 'POST','Content-Type': 'application/json', 'Authorization':"Bearer "+_tok}
payload = {'allycode': allycode, 
           'roster': True, 
           'project': {'name': True,
                       'members': True,
                       'gp':True,
                       'roster': {'name':True,
                                  'level': True,
                                  'allycode': True,
                                  'roster':{'defId': True,
                                            'rarity': True,
                                            'level': True,
                                            'gear': True
                         }}}}
data_url = urlBase+data_type['guild']#+str(allycode)
r = requests.request('POST',data_url, headers=head, data=dumps(payload), timeout = 1000)
data = loads(r.content.decode('utf-8'))

data_pg = data[0]['roster']
with open('data.json', 'w') as outfile:
    dump(data, outfile)
    
test = pd.DataFrame(data_pg[47]['roster'])


#PLAYER general
sign_url = urlBase+signin
payload = user
head = {"Content-type": "application/x-www-form-urlencoded",
        'Content-Length': str(len(payload))}
r = requests.request('POST',sign_url, headers=head, data=payload, timeout = 10)
if r.status_code != 200:
    error = 'Cannot login with these credentials'
_tok = loads(r.content.decode('utf-8'))['access_token']

data_url = urlBase+data_type['data']
payload = {'collection': 'unitsList'}
head = {'Method': 'POST','Content-Type': 'application/json', 'Authorization':"Bearer "+_tok, 'Content-Length': str(len(payload)) }

r = requests.request('POST',data_url, headers=head, data=dumps(payload), timeout = 1000)