# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:57:54 2018

@author: alessandro.rotatori
"""

import pandas as pd
import datetime

now = datetime.datetime.now()
now_date = str(now.year) + str(now.month) + str(now.day)
for i in range(len(data[0]['roster'])):
    tmp = pd.DataFrame(data[0]['roster'][i]['roster'])
    player_name = data[0]['roster'][i]['name']
    tmp['Guild_User'] = str(player_name)
    tmp['Date'] = str(now_date)
    if i == 0:
        character_list = pd.DataFrame(tmp)
    else:
        character_list.append(tmp, ignore_index =True)

del now, now_date, player_name, url_new, i
