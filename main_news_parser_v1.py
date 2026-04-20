# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:26:41 2023

@author: BTBdata
"""

import feedparser
import time
import datetime
import newspaper
import json
import pandas as pd

# EXPLORE RSS FEEDS
def get_rss_keys():
    feed = feedparser.parse("https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=1").keys()
    print("RSS FEED KEYS: ", feed)
    # get keys from feed
    #print("KEYS FRM FEED: ", feed.entries[0].keys())

#----------------------------------
# GET TITLE HASH ID
def hash_title(x):
    result = str(hash(x))
    return result

#----------------------------------
# PARSE DATA BY SOURCE    
def cnbc_data():
    date_now = datetime.datetime.now().date()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    parsed_date = str(date_now).replace("-",'') # fileDate
    file_name = timestr + '.csv'
    source = 'cnbc'
    cnbc_data = []
    cnbc_feeds = ["https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=100727362",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15837362",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19832390",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19794221",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10001147",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=15839135",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=20910258",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000664",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19854910",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000113",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000108",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=10000115",
    "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19836768"] 
    
    for i in cnbc_feeds:
        try:
            feed = feedparser.parse(i)
            for entry in feed.entries:
                cnbc_data.append(([hash_title(entry.title), parsed_date, entry.title, entry.summary, source]))               
        except:
            pass
    df = pd.DataFrame(cnbc_data, columns=["title_id","parsed_date","title","text","source"])     
    df.to_csv(Fr'C:BTBdata\raw_data2\{file_name}', encoding='utf-8', index=False) 
    
    
def cnn_data():
    date_now = datetime.datetime.now().date()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    parsed_date = str(date_now).replace("-",'') # fileDate
    file_name = timestr + '.csv'
    source = 'cnn'
    cnn_data = []
    cnn_feeds = ["http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://rss.cnn.com/rss/cnn_world.rss",
    "https://money.cnn.com/services/rss/",
    "https://www.cnn.com/services/rss/",
    "http://rss.cnn.com/rss/cnn_us.rss",
    "http://rss.cnn.com/rss/money_latest.rss",
    "http://rss.cnn.com/rss/cnn_allpolitics.rss",
    "http://rss.cnn.com/rss/cnn_tech.rss",
    "http://rss.cnn.com/rss/cnn_health.rss",
    "http://rss.cnn.com/rss/money_news_economy.rss",
    "http://rss.cnn.com/rss/money_news_international.rss",
    "http://rss.cnn.com/rss/money_news_companies.rss"] 
    
    for i in cnn_feeds:
        try:
            feed = feedparser.parse(i)
            for entry in feed.entries:
                cnn_data.append(([hash_title(entry.title), parsed_date, entry.title, entry.summary, source]))               
        except:
            pass
    df = pd.DataFrame(cnn_data, columns=["title_id","parsed_date","title","text","source"])     
    df.to_csv(Fr'C:\BTBdata\raw_data2\{file_name}', encoding='utf-8', index=False)  
    
    
    
def nytimes_data():
    date_now = datetime.datetime.now().date()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    parsed_date = str(date_now).replace("-",'') # fileDate
    file_name = timestr + '.csv'
    source = 'nytimes'
    nytimes_data = []
    nytimes_feeds = [
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/US.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Space.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Health.xml"] 
    
    for i in nytimes_feeds:
        try:
            feed = feedparser.parse(i)
            for entry in feed.entries:
                nytimes_data.append(([hash_title(entry.title), parsed_date, entry.title, entry.summary, source]))               
        except:
            pass
    df = pd.DataFrame(nytimes_data, columns=["title_id","parsed_date","title","text","source"])     
    df.to_csv(Fr'C:\BTBdata\raw_data2\{file_name}', encoding='utf-8', index=False) 
    
   
    
def cbs_data():
    date_now = datetime.datetime.now().date()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    parsed_date = str(date_now).replace("-",'') # fileDate
    file_name = timestr + '.csv'
    source = 'cbs'
    cbs_data = []
    cbs_feeds = ["https://www.cbsnews.com/latest/rss/us",
        "https://www.cbsnews.com/latest/rss/politics",
        "https://www.cbsnews.com/latest/rss/world",
        "https://www.cbsnews.com/latest/rss/health",
        "https://www.cbsnews.com/latest/rss/moneywatch",
        "https://www.cbsnews.com/latest/rss/science",
        "https://www.cbsnews.com/latest/rss/technology",
        "https://www.cbsnews.com/latest/rss/space"]
    
    for i in cbs_feeds:
        try:
            feed = feedparser.parse(i)
            for entry in feed.entries:
                cbs_data.append(([hash_title(entry.title), parsed_date, entry.title, entry.summary, source]))               
        except:
            pass
    df = pd.DataFrame(cbs_data, columns=["title_id","parsed_date","title","text","source"])     
    df.to_csv(Fr'C:\BTBdata\raw_data2\{file_name}', encoding='utf-8', index=False) 
    
    
    
def un_data():
    date_now = datetime.datetime.now().date()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    parsed_date = str(date_now).replace("-",'') # fileDate
    file_name = timestr + '.csv'
    source = 'un'
    un_data = []
    un_feeds = ["https://news.un.org/feed/subscribe/en/news/region/middle-east/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/region/africa/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/region/europe/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/region/americas/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/region/asia-pacific/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/health/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/un-affairs/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/law-and-crime-prevention/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/human-rights/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/humanitarian-aid/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/climate-change/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/economic-development/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/women/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/peace-and-security/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/migrants-and-refugees/feed/rss.xml",
        "https://news.un.org/feed/subscribe/en/news/topic/sdgs/feed/rss.xml"]
    
    for i in un_feeds:
        try:
            feed = feedparser.parse(i)
            for entry in feed.entries:
                un_data.append(([hash_title(entry.title), parsed_date, entry.title, entry.summary, source]))               
        except:
            pass
    df = pd.DataFrame(un_data, columns=["title_id","parsed_date","title","text","source"])     
    df.to_csv(Fr'C:\BTBdata\raw_data2\{file_name}', encoding='utf-8', index=False) 
    
    
def dod_data():
    date_now = datetime.datetime.now().date()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    parsed_date = str(date_now).replace("-",'') # fileDate
    file_name = timestr + '.csv'
    source = 'dod'
    dod_data = []
    dod_feeds = ["https://feeds.a.dj.com/rss/RSSWorldNews.xml",
        "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
        "https://feeds.a.dj.com/rss/RSSWSJD.xml",
        "https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?max=10&ContentType=1&Site=945"]
    
    for i in dod_feeds:
        try:
            feed = feedparser.parse(i)
            for entry in feed.entries:
                dod_data.append(([hash_title(entry.title), parsed_date, entry.title, entry.summary, source]))               
        except:
            pass
    df = pd.DataFrame(dod_data, columns=["title_id","parsed_date","title","text","source"])     
    df.to_csv(Fr'C:\BTBdata\raw_data2\{file_name}', encoding='utf-8', index=False) 
    

def politco_data():
    date_now = datetime.datetime.now().date()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    parsed_date = str(date_now).replace("-",'') # fileDate
    file_name = timestr + '.csv'
    source = 'politco'
    politco_data = []
    politco_feeds = ["http://rss.politico.com/congress.xml",
        "http://rss.politico.com/healthcare.xml",
        "http://rss.politico.com/defense.xml",
        "http://rss.politico.com/economy.xml",
        "http://rss.politico.com/energy.xml",
        "https://rss.politico.com/politics-news.xml"]
    
    for i in politco_feeds:
        try:
            feed = feedparser.parse(i)
            for entry in feed.entries:
                politco_data.append(([hash_title(entry.title), parsed_date, entry.title, entry.summary, source]))               
        except:
            pass
    df = pd.DataFrame(politco_data, columns=["title_id","parsed_date","title","text","source"])     
    df.to_csv(Fr'C:\BTBdata\raw_data2\{file_name}', encoding='utf-8', index=False) 
    
    
    
def sci_data():
    date_now = datetime.datetime.now().date()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    parsed_date = str(date_now).replace("-",'') # fileDate
    file_name = timestr + '.csv'
    source = 'sci'
    sci_data = []
    sci_feeds = ["https://www.sciencedaily.com/rss/all.xml",
        "https://www.sciencedaily.com/rss/top.xml",
        "https://www.sciencedaily.com/rss/top/science.xml",
        "https://www.sciencedaily.com/rss/top/health.xml",
        "https://www.sciencedaily.com/rss/top/technology.xml",
        "https://www.sciencedaily.com/rss/top/environment.xml",
        "https://www.sciencedaily.com/rss/most_popular.xml"]       
    
    for i in sci_feeds:
        try:
            feed = feedparser.parse(i)
            for entry in feed.entries:
                sci_data.append(([hash_title(entry.title), parsed_date, entry.title, entry.summary, source]))               
        except:
            pass
    df = pd.DataFrame(sci_data, columns=["title_id","parsed_date","title","text","source"])     
    df.to_csv(Fr'C:\BTBdata\raw_data2\{file_name}', encoding='utf-8', index=False) 
    

def main():
    cnbc_data()
    cnn_data()
    nytimes_data()
    cbs_data()
    un_data()
    dod_data()
    politco_data()
    sci_data()
    
main() 
