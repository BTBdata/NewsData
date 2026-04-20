# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 23:21:37 2023

@author: BTB Benjamin Bergenstein:
    script to fetch raw news articles and standardize them before pushing to database.
"""

import pandas as pd
import os
import datetime
import time

def prep_main_news():
    # dir of files to process
    directory = r'C:BTBdata\raw_text'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")        
        file_name = timestr + '.csv'  
        df = pd.read_csv(f,encoding='utf-8')   
    
        df.rename(columns={'text':'article_text', 'source':'source_type'}, inplace=True)
        df2 = df[['title_id', 'title','article_text','source_type','parsed_date']]
        df2.to_csv(Fr'C:BTBdata\push\{filename}', index=False)
 
def prep_bbc_news():
    # dir of files to process
    directory = r'C:BTBdataSolutions_Project\raw_bbc'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")        
        file_name = timestr + '.csv'  
        df = pd.read_csv(f,encoding='utf-8')     
        
        df.rename(columns={'title_hash':'title_id', 'summary':'article_text','type':'source_type'}, inplace=True)                         
        db = df[['title_id', 'title','article_text','source_type','parsed_date']]       
        db.to_csv(Fr'C:\BTBdata\push\{file_name}', index=False)
        
def main():
    #prep_main_news()
    prep_bbc_news()  


      
if __name__ == "__main__":
    main()
