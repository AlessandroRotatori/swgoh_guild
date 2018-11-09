# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:54:12 2018

@author: alessandro.rotatori
"""
import pandas as pd

# LISTA DI TOON NUOVA GILDA
final_toon_list = pd.merge(character_list, map_id_name, how = 'left', 
                           left_on = 'defId', right_on = 'base_id')
final_toon_list = final_toon_list[['Date', 'Guild_User', 'defId', 'name', 'gp','level', 'rarity', 'gear']]

# VERIFICA DEI TEAM PER NUOVA LISTA
details_team_ng = pd.merge(df_tw_std, final_toon_list, how = 'inner',
                          left_on = 'value', right_on = 'name')

total_team_ng = details_team_ng.groupby(['Guild_User','CLASSE', 'ID_TEAM'], as_index = False)[['gp']].sum()
group = ['Guild_User', 'CLASSE']
selects = ['Guild_User', 'CLASSE', 'gp', 'ID_TEAM']
best_team_ng = total_team_ng.groupby(group, as_index=False).apply(lambda s: s.loc[s.gp.idxmax(), selects]).reset_index(drop=True)

#SCRITTURA EXCEL
writer = pd.ExcelWriter('little_group_data.xlsx', engine='xlsxwriter')
final_toon_list.to_excel(writer, sheet_name='total_toon')
pd.DataFrame(tw_std_teams).to_excel(writer, sheet_name='standard_teams')
best_team_ng.to_excel(writer, sheet_name='results')
writer.save()