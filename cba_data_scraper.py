# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 07:54:04 2021

@author: owner
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml 
import datetime
import time as tt
import numpy as np


ASX_CODE = ['ABP','ABC','APT','RIO','AGL','ALQ','ALU','AWC','AMC','AMP','ANN','APE','APA','APX','ARB']

df = pd.DataFrame()
df['Code'] = 0
df['Price'] = 0
df['Time'] = 0
df['Date'] = 0

i = 0
now_hour =0


time_delay = 60   
while now_hour<15:
    for stock in range(0,len(ASX_CODE)):
        i = i + 1
        asx_code = ASX_CODE[stock]
        now = datetime.datetime.today()
        now_today = datetime.date(now.year,now.month,now.day)
        now_hour = now.hour
        time = datetime.time(now.hour,now.minute,now.second)
        url = f'https://au.finance.yahoo.com/quote/{asx_code}.AX?p={asx_code}.AX&.tsrc=fin-srch'
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        for info in soup.find_all("div", class_ = "D(ib) Mend(20px)"):
            price = info.span.text
            df.loc[i,'Code']=asx_code
            df.loc[i,'Price']=price
            df.loc[i, 'Time'] = time
            df.loc[i, 'Date'] = now_today
    file_name = f'ASX_Data_{now_today}.xlsx'
    sheetname = file_name
    df.to_excel(file_name, sheet_name = sheetname)
    tt.sleep(time_delay)
    
    


