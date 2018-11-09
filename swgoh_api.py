# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:44:40 2018

@author: alessandro.rotatori
"""

import requests
from json import loads, dumps, dump

class SWGOHhelp():
    def __init__(self, settings):
        self.user = "username="+settings.username     
        self.user += "&password="+settings.password
        self.user += "&grant_type=password"
        self.user += "&client_id="+settings.client_id
        self.user += "&client_secret="+settings.client_secret
        self.urlBase = 'https://api.swgoh.help'
        self.signin = '/auth/signin'
        self.data_type = {'guild':'/swgoh/guild/',
                          #'player':'/swgoh/player/',
                          'data':'/swgoh/data/'}
    def get_token(self):
        sign_url = self.urlBase+self.signin
        payload = self.user
        head = {"Content-type": "application/x-www-form-urlencoded",
                'Content-Length': str(len(payload))}
        r = requests.request('POST',sign_url, headers=head, data=payload, timeout = 10)
        if r.status_code != 200:
            error = 'Cannot login with these credentials'
            return  {"status_code" : r.status_code,
                     "message": error}
        _tok = loads(r.content.decode('utf-8'))['access_token']
        self.token = { 'Authorization':"Bearer "+_tok} 
        return(self.token)
    
    def get_data(self, _data_type, _spec):
        #creazione header
        token = self.get_token()
        head = {'Method': 'POST', 'Content-Type': 'application/json'}
        head.update(token)
        #creazione url
        data_url = self.urlBase+self.data_type[_data_type]
        #creazione payload
        if _data_type == 'guild':
                payload = {'allycode': _spec, 
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
                                                            'gear': True,
                                                            'gp': True
                         }}}}
        try:
            r = requests.request('POST', data_url, headers=head, data = dumps(payload), timeout = 1000)
            if r.status_code != 200:
                error = 'Cannot fetch data - error code'
                data = {"status_code" : r.status_code,
                         "message": error}
            data = loads(r.content.decode('utf-8'))
        except:
            data = {"message": 'Cannot fetch data'}
        return data

class settings():
    def __init__(self, _username, _password, _client_id, _client_secret):
        self.username = _username
        self.password = _password
        self.client_id = _client_id
        self.client_secret = _client_secret
        
#your username and password here, remaining two (client and client secret) are not used so far so filling anything
creds = settings('ObiAle','alex87rot','123','abc')
client = SWGOHhelp(creds)

#player data
#allycode = 163532549
#data = client.get_data('guild', allycode)
#print(player)

#new guild
allycode = 127992866
data_new_guild = client.get_data('guild', allycode)

with open('litte_group_data.json', 'w') as outfile:
        dump(data_new_guild, outfile)
