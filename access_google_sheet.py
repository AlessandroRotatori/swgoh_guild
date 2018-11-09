# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:01:06 2018

@author: alessandro.rotatori
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("TEAM_MAPPING").sheet1

# Extract and print all of the values
tw_std_teams = sheet.get_all_records()
# print(tw_std_teams)

#generate data frame
df_tw_std = pd.DataFrame(tw_std_teams)
df_tw_std = pd.melt(df_tw_std, id_vars = ['CLASSE', 'ID_TEAM'], value_vars = ['CHAR_1',
                                                                    'CHAR_2',
                                                                    'CHAR_3',
                                                                    'CHAR_4',
                                                                    'CHAR_5'])
df_tw_std = df_tw_std.drop(columns='variable')

with open('tw_std_teams.json', 'w') as outfile:
    json.dump(df_tw_std1, outfile)
    