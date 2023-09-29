# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:01:50 2023

@author: BTB
"""

import pandas as pd
from BBCHeadlines import news
import datetime


def hash_title(x):
    result = str(hash(x))
    return result

def get_bbc_headlines():
    results = news() 
    
    date_now = datetime.datetime.now().date()
    file_date = str(date_now).replace("-",'')
    time_now = datetime.datetime.now().time()
    df = pd.DataFrame.from_dict(results) 
    df['parsed_date'] = date_now
    df['parsed_time'] = time_now
    df['type'] = 'short article'
          
    df['title_hash'] = df['title'].astype(str).apply(lambda x: hash_title(x))  
    
    df2 = df[['title','summary','published','parsed_date','parsed_time','type', 'title_hash']]
    file_name = file_date + '.csv'
    # local
    #df2.to_csv(rf'C:\Users\benja\OneDrive\Documents\BTBdataSolutions_Project\data_dfs/{file_name}', index=False)
    # google drive
    df2.to_csv(f'/content/drive/My Drive/BTBdataSolutions_ArticleData/{file_name}', index=False)
get_bbc_headlines()
