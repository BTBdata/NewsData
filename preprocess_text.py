# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 01:35:52 2023

@author: BTB Data Solutions - Ben Bergenstein
"""
import nltk
import string
import re
import os
import time
import datetime
import pandas as pd
from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import spacy
nlp = spacy.load('en_core_web_md')

# make all text lowercase
def lower_text(x):
    lower = x.lower()
    return lower
    
# Remove numbers
def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result

# remove whitespace
def remove_whitespace(text):
    return  " ".join(text.split())
 
# remove stopwords
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    text_rslt =  ' '.join([word for word in text.split() if word not in stop_words]) 
    return text_rslt
 
# lemmatize words
def lemmatize_words(text):
    doc = nlp(text)
    for token in doc:   
        text_rslt =  ' '.join([token.lemma_ for token in doc]) 
        return text_rslt
       
def read_in_docs():
    # read docs in from ner_out
    directory = r'C:\Users\benja\OneDrive\Documents\BTBdataSolutions_Project\ner_out'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")        
        file_name = timestr + '.csv'  
        df = pd.read_csv(f,encoding='utf-8')  
        # lower
        df['lower'] = df['text_merged'].apply(lambda x: lower_text(x))
        # convert numbers to text
        df['num_text'] = df['lower'].apply(remove_numbers)
        # remove punctuation
        df['merged_text_clean'] = df['num_text'].str.replace('[^\w\s]', '', regex=True)
        # remove whitespace
        df['clean_text'] = df['merged_text_clean'].apply(lambda x: remove_whitespace(x))
        # no stopwords
        df['clean_no_stopwords'] = df['clean_text'].apply(lambda x: remove_stopwords(x))
        # lemitization
        df['clean_no_stop_lemmatized'] = df['clean_no_stopwords'].apply(lambda x: lemmatize_words(x))
        
        df = df[["title_id", "parsed_date", "source", "people", "norp", "fac",
                     "org", "gpe", "loc", "product", "event","title","text", "clean_text",
                     "clean_no_stopwords", "clean_no_stop_lemmatized"]]
        df.to_csv(Fr'C:\Users\benja\OneDrive\Documents\BTBdataSolutions_Project\clean_text\{file_name}', index=False)
               
read_in_docs()  
