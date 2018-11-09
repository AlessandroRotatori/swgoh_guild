# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:57:54 2018

@author: alessandro.rotatori
"""

import pandas as pd
import datetime

now = datetime.datetime.now()
for i in range(len(data_new_guild[0]['roster'])):
    tmp = pd.DataFrame(data_new_guild[0]['roster'][i]['roster'])
    player_name = data_new_guild[0]['roster'][i]['name']
    tmp['Guild_User'] = str(player_name)
    tmp['Date'] = now
    if i == 0:
        character_list = pd.DataFrame(tmp)
    else:
        frames = [character_list, tmp]
        character_list = pd.concat(frames)

del now, player_name, i, tmp
