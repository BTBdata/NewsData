
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:51:36 2023

@author: BTB Data Solutions, Ben Bergenstein

NLP Text Preprocessing and NER parser.
"""
import pickle as pkl
import spacy
import pandas as pd
import numpy as np
import os
import time
import datetime
import re
from textblob import TextBlob
# sentiment
import flair
# graph
import textacy
# text preprocessing
import nltk
import string
import datetime
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize 
import nltk.data 
# num to words
import inflect

# broad topic 
from sklearn.neighbors import NearestNeighbors
from scipy import spatial
# broad topic
from corextopic import corextopic as ct
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from scipy import spatial
#from keybert import KeyBERT
from corextopic import vis_topic as vt

import os, shutil

# Importing libraries 
import nltk 
import re 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import pandas as pd

import yake
import textacy
import matplotlib.pylab as plt
import networkx as nx
import unicodedata

nlp = spacy.load('en_core_web_md')

def end_sents(x):
    end = x + '.'
    return end

# not used
def sent(x):
    blob = TextBlob(x)
    a = blob.sentiment
    return a

################################### NOUN PHRASES #########################
def noun_chunks_return(x):
    blob = TextBlob(x)
    a = blob.noun_phrases
    return a

################################### NAME ENTITY RECOGNITION ##############
def ner_extraction(data):
    ent_list = []
    people = []
    norp = []
    fac = []
    org = []
    gpe = []
    loc = []
    product = []
    event = []
    # Added 10/23
    date = []
    percent = []
    quant = []
    ordinal = []
    money = []
    cardinal = []
    black_list = ["LANGUAGE", "TIME", "WORK_OF_ART"]
    #nlp = spacy.load('en_core_web_md')     
    doc = nlp(str(data))
    for ent in doc.ents:    
        if ent.label_ == 'PERSON' and ent.label_ not in black_list:
            people.append(ent.text)
        if ent.label_ == 'NORP' and ent.label_ not in black_list:
            norp.append(ent.text)
        if ent.label_ == 'FAC' and ent.label_ not in black_list:
            fac.append(ent.text)       
        if ent.label_ == 'ORG' and ent.label_ not in black_list:
            org.append(ent.text)  
        if ent.label_ == 'GPE' and ent.label_ not in black_list:
            gpe.append(ent.text)
        if ent.label_ == 'LOC' and ent.label_ not in black_list:
            loc.append(ent.text) 
        if ent.label_ == 'PRODUCT' and ent.label_ not in black_list:
            product.append(ent.text)   
        if ent.label_ == 'EVENT' and ent.label_ not in black_list:
            event.append(ent.text)           
        if ent.label_ == 'DATE' and ent.label_ not in black_list:
            date.append(ent.text)       
        if ent.label_ == 'PERCENT' and ent.label_ not in black_list:
            percent.append(ent.text)  
        if ent.label_ == 'QUANTITY' and ent.label_ not in black_list:
            quant.append(ent.text)
        if ent.label_ == 'ORDINAL' and ent.label_ not in black_list:
            ordinal.append(ent.text) 
        if ent.label_ == 'MONEY' and ent.label_ not in black_list:
            money.append(ent.text)   
        if ent.label_ == 'CARDINAL' and ent.label_ not in black_list:
            cardinal.append(ent.text)   
        else:
            pass
    peopleb = list(set(people))
    norpb = list(set(norp))
    facb = list(set(fac))
    orgb = list(set(org))
    gpeb = list(set(gpe))
    locb = list(set(loc))
    productb = list(set(product))
    eventb = list(set(event))
    dateb = list(set(date))
    percentb = list(set(percent))
    quantb = list(set(quant))
    ordinalb = list(set(ordinal))
    moneyb = list(set(money))
    cardinalb = list(set(cardinal))

    #print(peopleb)
    return peopleb, norpb, facb,orgb, gpeb, locb, productb,eventb,dateb,percentb,quantb,ordinalb,moneyb,cardinalb

########################## CLEAN FOLDERS ##########################
def del_contents(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
                    
def clean_folders():    
    ner_out = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\ner_out'
    clean_out = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\clean_out'
    ner_temp = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\ner_temp'
    sent_out = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\sent_out'
    
    dirs = [ner_out, clean_out, ner_temp, sent_out]
    for i in dirs:
        i2 = str(i)
        del_contents(i2)
            
###################### START ########################## 
def read_in_docs_NER():
    # dir of files to process
    directory = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\raw_text'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")        
        file_name = timestr + '.csv'  
        df = pd.read_csv(f,encoding='utf-8')        
        # add period to title b4 merging
        df['new_title'] = df['title'].apply(end_sents)
        # merge 2 cols into 1 col
        #df['text_merged'] = df[['new_title', 'text']].apply(lambda x: ' '.join(x), axis=1)
        # updated column merge 11/2023
        df['text_merged'] = df['new_title'] + '. ' + df['article_text']
        # join multiple lists into separate cols
        df["people"],df["norp"],df["fac"],df["org"],df["gpe"],df["loc"],df["product"],df["event"],df['date'],df['percent'],df['quant'],df['ordinal'],df['money'],df['cardinal'] = zip(*df["text_merged"].map(ner_extraction))
        
        df.to_csv(Fr'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\ner_temp\{file_name}', index=False)
           
def clean_ner():
    directory = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\ner_temp'  
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        df = pd.read_csv(f,encoding='utf-8') 
        # clean up NEW columns (keep only words and , )
        df['people'] = df['people'].str.replace('[^\w\s,]', '', regex=True)
        df['norp'] = df['norp'].str.replace('[^\w\s,]', '', regex=True)
        df['fac'] = df['fac'].str.replace('[^\w\s,]', '', regex=True)
        df['org'] = df['org'].str.replace('[^\w\s,]', '', regex=True)
        df['gpe'] = df['gpe'].str.replace('[^\w\s,]', '', regex=True)
        df['loc'] = df['loc'].str.replace('[^\w\s,]', '', regex=True)
        df['product'] = df['product'].str.replace('[^\w\s,]', '', regex=True)
        df['event'] = df['event'].str.replace('[^\w\s,]', '', regex=True)
        expr = r"[\'\[\]\"]"
        df['date'] = df['date'].str.replace(expr, '', regex=True)
        df['percent'] = df['percent'].str.replace(expr, '', regex=True)
        df['quant'] = df['quant'].str.replace(expr, '', regex=True)
        df['ordinal'] = df['ordinal'].str.replace(expr, '', regex=True)
        df['money'] = df['money'].str.replace(expr, '', regex=True)
        df['cardinal'] = df['cardinal'].str.replace(expr, '', regex=True)
        
        df.to_csv(Fr'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\ner_out\{filename}', index=False)
        print('NER complete')

######################### SENTIMENT FLAIR DISTILBERT ###############################

model = flair.models.TextClassifier.load('en-sentiment')

def get_sent(x):
    sentence = flair.data.Sentence(str(x))
    model.predict(sentence)
    sentiment = sentence.labels[0].value
    score = sentence.labels[0].score
    return sentiment, score

def sentiment_text():   
    # dir of files to process
    directory = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\ner_out'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")        
        file_name = timestr + '.csv'  
        df = pd.read_csv(f,encoding='utf-8')       
        df['sentiment_direction'],df['sentiment_score'] = zip(*df['text_merged'].map(get_sent))    
        df.to_csv(Fr'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\sent_out\{filename}', index=False)


def hyphen(x): 
    rslt = x.replace("-"," ")
    return rslt
def comma(x):
    rslt = x.replace(","," ")
    return rslt

# remove whitespace
def remove_whitespace(text):
    return  " ".join(text.split())

############################# YAKE ##########################    
def yake_keywords(text):
    kw_extractor = yake.KeywordExtractor()
    language = "en"
    max_ngram_size = 5
    deduplication_threshold = 0.1
    numOfKeywords = 4
    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
    result = custom_kw_extractor.extract_keywords(text)   
    for kw in result:
        return kw
    
###################### TEXT PREPROCESSING & NOUN PHRASE #################################

# make all text lowercase
def lower_text(x):
    lower = x.lower()
    return lower

# Remove numbers
def remove_numbers(text):
    result = re.sub(r'\d+', '', text)
    return result

# remove whitespace
def remove_whitespace2(text):
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
 
import re
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

def remove_accents(x):
    x = str(x)
    nfkd_form = unicodedata.normalize('NFKD', x)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def clean_text():
    # read docs in from ner_out
    directory = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\sent_out'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)      
        df = pd.read_csv(f,encoding='utf-8')  
        # drop duplications
        df.drop_duplicates(subset='text_merged',keep='first', inplace=True)   
        # remove special chars
        #df['Text'] = df.Text.astype(str).apply(lambda x: re.sub('[^A-Za-z0-9.]+', ' ',x))
        
        # remove accents
        df['accent'] = df['text_merged'].apply(remove_accents)
        # remove hyphen add space
        df['hyphen'] = df['accent'].apply(hyphen)
        # lower
        df['lower'] = df['hyphen'].apply(lambda x: lower_text(str(x)))  
        
        # remove emojis
        df['emoji_text'] = df['lower'].apply(remove_emojis) 
        # remove punctuation
        df['text_clean'] = df['emoji_text'].str.replace('[^\w\s]', '', regex=True)
        # convert numbers to text
        df['num_text'] = df['text_clean'].apply(remove_numbers)    
        # remove whitespace
        df['clean_text'] = df['num_text'].apply(lambda x: remove_whitespace(x))     
        # no stopwords
        df['clean_no_stopwords'] = df['clean_text'].apply(lambda x: remove_stopwords(x))
        # lemitization
        df['clean_no_stop_lemmatized'] = df['clean_no_stopwords'].apply(lambda x: lemmatize_words(x))   
        
        ########### noun_chunks ###########
        df['noun_phrase'] = df['clean_no_stopwords'].apply(noun_chunks_return)
        
        ########### YAKE KEYWORDS #########
        df['keywords'] = df['clean_no_stopwords'].apply(yake_keywords)
        
        
        # clean up not used columns 
        df = df.drop(columns=['hyphen', 'accent','lower','num_text','text_clean', 'emoji_text', 'new_title', 'text_merged',
                               'title', 'article_text'])
             
        df.to_csv(Fr'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\clean_out\{filename}', index=False, encoding='utf-8')       
  
######################################### TOPIC MODELING 1 #######################################
# Government/politics Health Sports Education Business/Finance
# Humanitarian Climate Entertainment Crime/Legal Conflict Tension
        
def map_topics(tag):
    entertainment = ['movies','music','art']
    sports = ['sports', 'games']
    govt_politics = ['government','politics']
    conflict = ['war']
    business_finance = ['stock', 'financial']

    if tag in entertainment:
        tag1 = 'entertainment'
        return tag1
    if tag in sports:
        tag2 = 'sports'
        return tag2
    if tag in govt_politics:
        tag3 = 'government_politics'
        return tag3
    if tag in conflict:
        tag4 = 'conflict'
        return tag4
    if tag in business_finance:
        tag5 = 'business_finance'
        return tag5
    else:
        return tag
        
#  embed words for classification # 
def embed(tokens, nlp):  
    lexemes = (nlp.vocab[token] for token in tokens)

    vectors = np.asarray([
        lexeme.vector
        for lexeme in lexemes
        if lexeme.has_vector
        and not lexeme.is_stop
        and len(lexeme.text) > 1
    ])

    if len(vectors) > 0:
        centroid = vectors.mean(axis=0)
    else:
        width = nlp.meta['vectors']['width']
        centroid = np.zeros(width)

    return centroid

# unsupervised classification for topic extraction # 
def predict(text):
     
    try:
      # aa & html are to help screen trash
        doc = text
        # tuned 10/29/2023
        label_names = ['sports','games', 'movies', 'music', 'humanitarian', 'financial', 'technology', 'health', 'crime', 'war','education', 'art', 'government', 'politics', 'stock', 'aa']
        label_vectors = np.asarray([embed(label.split(','), nlp)for label in label_names])                
        #print(label_vectors.shape)
        neigh = NearestNeighbors(n_neighbors=1, metric=spatial.distance.cosine)
        neigh.fit(label_vectors)        
        tokens = doc.split(' ')
        centroid = embed(tokens, nlp)
        closest_label = neigh.kneighbors([centroid], return_distance=False)[0][0]       
        print('Label: ', label_names[closest_label])
        return label_names[closest_label]
    except:
        return 'float'

def get_preds():
    # read docs
    timestr = time.strftime("%Y%m%d_%H%M%S")         
    directory = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\clean_out'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        df = pd.read_csv(f,encoding='utf-8')   
        doc = df['clean_no_stopwords'].astype(str)    
        df['sub_topic'] = df['clean_no_stopwords'].apply(lambda doc: predict(doc))   
        # map topics
        df['broad_topic_out'] = df['sub_topic'].apply(map_topics)
        # drop columns not needed
        #df = df.drop(columns=['clean_no_stopwords'])
        # to csv
        df.to_csv(Fr'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\out\nlp_bv1_{timestr}.csv', index=False)

###################################################################

###################################################################
def main():
    clean_folders()
    read_in_docs_NER() 
    clean_ner()
    sentiment_text()
    clean_text()
    get_preds()
    
##################### RUN SCRIPT ##############################
if __name__ == "__main__":
    main()
    
