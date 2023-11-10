# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 23:21:37 2023

@author: BTB Data Solutions - Benjamin Bergenstein:
    script to fetch raw news articles and standardize them before pushing to database.
"""

import pandas as pd
import os
import datetime
import time
import uuid

# change 11/9/2023:added uuid to each record

def generate_uuid():
    id = uuid.uuid4()
    return id
    
def prep_main_news():
    uuid1 = []
    # dir of files to process
    directory = r'C:\Users\Administrator\Documents\raw_api_news_main'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        df = pd.read_csv(f,encoding='utf-8')   
        # add uuid
        for i in range(len(df.index)):
            rslt = generate_uuid()
            uuid1.append(rslt)
        df['article_id'] = pd.Series(uuid1)
        df.rename(columns={'text':'article_text', 'source':'source_type'}, inplace=True)
        df2 = df[['article_id', 'title_id', 'title', 'article_text', 'source_type', 'parsed_date']]
        df2.to_csv(Fr'C:\Users\Administrator\Documents\push_raw_news\{filename}', index=False)
 
def prep_bbc_news():
    uuid2 = []
    # dir of files to process
    directory = r'C:\Users\Administrator\Documents\raw_news_articles'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        df = pd.read_csv(f,encoding='utf-8')     
        # add uuid
        for i in range(len(df.index)):
            rslt = generate_uuid()
            uuid2.append(rslt)
        df['article_id'] = pd.Series(uuid2)
        df.rename(columns={'title_hash':'title_id', 'summary':'article_text','type':'source_type'}, inplace=True)                         
        db = df[['article_id', 'title_id', 'title', 'article_text','source_type', 'parsed_date']]       
        db.to_csv(Fr'C:\Users\Administrator\Documents\push_raw_news\{filename}', index=False)
        
def main():
    prep_main_news()
    prep_bbc_news()  


      
if __name__ == "__main__":
    main()
