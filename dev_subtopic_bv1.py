# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:28:54 2024

@author: benja
"""
import numpy as np
import spacy
import textacy 
from spacy.matcher import PhraseMatcher
import pandas as pd
import re
import os
import time
from iso_codes_bv1 import *

nlp = spacy.load("en_core_web_md")
matcher = PhraseMatcher(nlp.vocab)


def bbow_phrases(x):
    
    ## BBOW PHRASE MATCHER ##
    big_bag_of_words = ['diplomatic', 'abduct', 'abduction', 'abomination', 'abuse', 'account', 'accuse', 'acls', 
             'acquire', 'activism', 'actor', 'actress', 'advancement', 'agree', 'agreement', 'ai', 'aid worker',
             'air', 'air force', 'air strike', 'aircraft carrier', 'album', 'ambassador', 'ambulance', 
             'ammunition', 'anger', 'angry', 'animal', 'antisemitism', 'archaeologist', 'argue', 'argument',
             'army', 'arrest', 'artificial intelligence', 'ash', 'assault', 'assert', 'asteroid', 'astronaut', 
             'athletic', 'atrocity', 'attack', 'auto', 'automobile', 'automotive', 'avalanche', 'avow', 
             'bank bank', 'banking', 'baseball', 'basketball', 'bass', 'bassist', 'battle', 'beaufort scale', 
             'bed and breakfast', 'behead', 'bipartisan', 'bird', 'bird flu', 'black jack', 'blackmail', 
             'blackout', 'blizzard', 'blood supply', 'bloodshed', 'bnb', 'bowl', 'bribe', 'bronze metal', 
             'brutality', 'burglary', 'business', 'business model', 'business strategy', 'campaign', 'campus',
             'cancer', 'carbon emission', 'casualty', 'casualty of war', 'cat', 'ceasefire', 'ceo', 
             'championship', 'chemical', 'chemical warfare', 'cinematic', 'claim', 'clarinet', 'class of', 
             'classroom', 'clean energy', 'climate change', 'cocaine', 'cold', 'college', 'colonel', 'combat',
             'competition', 'competitive analysis', 'computer hacker', 'concert', 'conflict', 
             'conflict resolution', 'conflict zone', 'congress', 'consult', 'contend', 'convict', 'cop', 'corn', 
             'corporate', 'corruption', 'counter attack', 'court rulling', 'covid', 'cow', 'cpu', 'crack', 'crime',
             'criminal investigation', 'criminal offence', 'criminal procedure', 'criminal profiling', 'crisis',
             'crop', 'curriculum', 'customer service', 'cybercrime', 'damage', 'dart', 'dead', 'death', 
             'debate', 'decease', 'defeat', 'defense', 'demise', 'democrats', 'depart', 'destination wedding',
             'detective', 'diabetes', 'diagnose', 'diagnosis', 'digital marketing', 'dinosaur', 'disability',
             'disagree', 'disaster', 'disaster preparedness', 'disaster risk reduction', 'discuss', 'discussion',
             'disease', 'dispute', 'distance learning', 'doctor', 'dog', 'domestic violence', 'drone',
             'drone air strike', 'drought', 'drug', 'drug addiction', 'drug offense', 'drug trafficking', 
             'drummer', 'duck', 'e commerce', 'e learn', 'early childhood education', 'earth', 'economic',
             'education', 'el nina', 'el nino', 'elderly', 'election', 'electric vehicle', 'electrocution',
             'elementary school', 'embezzle', 'embezzlement', 'emergency', 'emergency room', 'emotion',
             'energy', 'entertainment', 'entrepreneurial', 'environment', 'er', 'eruption', 'escalate',
             'escalation of violence', 'espionage', 'espn', 'evacuate', 'evacuation', 'evidence', 
             'exploration', 'explosion', 'export', 'expostulate', 'extort', 'extortion', 'fall', 'farm',
             'fatal', 'fatal shooting', 'fault', 'fbi', 'felony', 'feud', 'fight', 'film', 'finance', 'fire',
             'first aid', 'first place', 'flank', 'flood', 'flu', 'flu season', 'flu shoot', 'fly', 'food',
             'food aid', 'food supply', 'football', 'forecast', 'forensic', 'fraud', 'freedom', 'freeze',
             'frontline', 'fuel', 'game', 'gang war', 'gas', 'gas mask', 'gas price', 'general', 'genocide',
             'global trade', 'global warming', 'gold medalist', 'golf', 'gorilla warfare', 'gpa', 'gpt',
             'grade', 'graduate', 'graduation', 'ground operation', 'guerilla warfare', 'guilty', 'guitar', 
             'guitarist', 'hacker', 'hate crime', 'health', 'health care', 'healthcare record', 'heat', 
             'heat wave', 'heavy rain', 'heinous act', 'heist', 'high education', 'high pressure', 'high rate',
             'highjack', 'hippa', 'hockey', 'hog', 'hold captive', 'hollywood', 'homicide', 'horse', 'hospital',
             'hostage', 'housing market', 'human resource', 'human trafficking', 'humanitarian aid', 'hurricane',
             'ide', 'identity theft', 'ill', 'illegal', 'illness', 'impersonate', 'import export',
             'importation', 'imprisonment', 'industrial', 'industry', 'infanticide', 'inhumane', 
             'injure', 'innovation', 'insect', 'insist', 'insurance fraud', 'insurgent', 'intellectual property',
             'interception', 'internally displace person', 'introduce bill', 'introduce new bill', 
             'investigate', 'investigation', 'investment', 'jail', 'jet', 'judicial', 'juvenile delinquent',
             'kidnap', 'kidney', 'kill', 'killer', 'labor market', 'lake', 'landslide', 'language model',
             'larceny', 'last place', 'launch an attack', 'law', 'law enforcement', 'leadership', 'legal',
             'legal system', 'legislature', 'life imprisonment', 'lifelong learning', 'lightning', 'literacy',
             'low rate', 'lsd', 'machine learning', 'mafia', 'malefaction', 'manufacturing', 'marijuana',
             'marine', 'market research', 'marketing', 'md', 'mediate', 'medical assistance', 'medical board',
             'medical help', 'medical record', 'medication', 'merger', 'meteor', 'militant', 'military', 
             'misdemeanor', 'missile', 'ml', 'mobilization', 'money laundering', 'mortgage', 'movie', 
             'movie star', 'murder', 'music', 'music video', 'musician', 'narcotic', 'nasa', 'nascar',
             'nato', 'navy', 'negotiate', 'new release', 'new technology', 'nlp', 'nuclear',
             'nuclear warfare', 'nuclear weapon', 'numeracy', 'nurse', 'nurse aid', 'nursing', 
             'nursing home', 'ocean', 'offence', 'offender', 'offense', 'officer', 'oil', 'olimpics',
             'olympic', 'online education', 'opera', 'operate', 'operation', 'optical', 'order', 
             'organize crime', 'outer space', 'overtake', 'oxycontin', 'pandemic', 'paramedic', 
             'pass away', 'peace', 'peace corps', 'peace negotiation', 'peacekeeping', 'peacetime negotiation',
             'pedagogy', 'perish', 'perpetrator', 'piano', 'pig', 'ping pong', 'pitch', 
             'plaintiff', 'plane', 'planet', 'plead', 'plumet', 'poker', 'police', 'pollute', 
             'pollution', 'pool', 'post conflict', 'pow', 'power lifting', 'prescription', 'price increase', 
             'price soar', 'price thrive', 'prison', 'prisoner of war', 'produce', 'project management',
             'prostitution', 'punishable', 'punishment', 'punitive damage', 'quarrel', 'race', 'racketeering',
             'radioactive', 'rain', 'ransom', 'rape', 'real estate', 'record', 'red cross', 'refugee',
             'rehabilitation', 'relief', 'renewable energy', 'republican', 'restaurant', 'retail', 'revenue',
             'rise', 'risk management', 'rivalry', 'robbery', 'sale', 'sanitation', 'satellite', 'school',
             'scientist', 'second place', 'secondary education', 'security', 'sentence', 'sergeant', 
             'serial killer', 'series', 'setback', 'sex offence', 'sexual', 'sexual violence', 
             'sexually assault', 'shelter', 'shoot', 'shoot out', 'shotput', 'shuttle', 'sick',
             'sickness', 'side effect', 'silver metal', 'singer', 'sirus', 'slain', 'slay', 
             'small business', 'smoke', 'snow', 'soccer', 'solar', 'solder', 'song', 'space',
             'spacecraft', 'sport medicine', 'sport medium', 'squabble', 'startup', 'state', 
             'state of the art', 'statutory', 'steal', 'stock market', 'stock price', 'strike', 
             'student', 'submarine', 'succession', 'summer sport', 'supply chain', 'surgeon',
             'surgeon general', 'surgery', 'surrender', 'suspect', 'sustainability', 
             'sustainable development', 'tactic', 'tank', 'teaching', 'technology', 'rebel',
             'technology count', 'tennis', 'tension', 'tension rise', 'terminal ill', 
             'terrorism', 'terrorist activity', 'terrorist activityfood and water', 'terrorist group', 
             'theft', 'thief', 'third place', 'tornado', 'touchdown', 'trade', 'tragedy', 'trans gender', 
             'transgression', 'travel', 'treatment', 'trend', 'troop', 'tsunami', 'tv', 'unemployment',
             'uniform', 'universe', 'unlawful', 'unlivable condition', 'upset', 'us space force', 
             'usaid', 'vacation', 'vaccination', 'vaccine', 'vagrancy', 'vandalism', 'vegetation', 
             'veteran', 'victim', 'victory', 'video game', 'violence', 'violent protest', 'virus',
             'volcano', 'voter', 'vulnerable population', 'war', 'war crime', 'wartime', 'water', 
             'water level', 'weapon', 'weapon of mass destruction', 'weather', 'weight lifting', 
             'whale', 'white collar crime', 'white out', 'wild life', 'wildfire', 'win', 'wind', 
             'windstorm', 'winter sport', 'witness', 'witness protection', 'x ray']
         
    
    big_bag_of_words = set(big_bag_of_words)
    #obtain doc object for each word in the list and store it in a list
    patterns = [nlp(sub) for sub in big_bag_of_words]
    #add the pattern to the matcher
    matcher.add("SUBTOPIC_PATTERN", patterns)
    #process some text
    x = str(x)
    doc = nlp(x)
    matches = matcher(doc)
    items = []
    for match_id, start, end in matches:    
        span = doc[start:end]
        items.append(span.text)
    rslt = set(items)
    print(rslt)
    return rslt
    
    ## TEXTACY KEY TERMS ##
def parse_keywords(text):
    text = str(text)
    doc = nlp(text)
    key = textacy.extract.keyterms.sgrank(doc, ngrams=(1, 2),normalize='lemma', topn=1)
    #key2 = textacy.extract.triples.subject_verb_object_triples(doc)
    return key
  
    ## CLEAN RESULTS ##
def clean_bbow_results(x): 
    rslt1 = x.replace("{","")
    rslt2 = rslt1.replace("}", "")
    rslt3 = rslt2.replace("'", "")
    rslt4 = rslt3.replace("set()", "")
    rslt5 = rslt4.replace(",", " ,")
    rslt6 = " ".join(rslt5.split())
    return rslt6
    
     ## CLEAN KEY PHRASES
def clean_keyterm_results(x): 
    rslt1 = x.replace("[","")
    rslt2 = rslt1.replace("]", "")
    rslt3 = rslt2.replace("'", "")
    rslt4 = rslt3.replace("(", "")
    rslt5 = rslt4.replace(")", "")
    rslt6 = rslt5.replace(".", "")
    rslt7 = rslt6.replace(",", "")
    rslt8 = re.sub(r'\d+', '', rslt7)
    rslt9 = " ".join(rslt8.split())
    return rslt9

    ## CLEAN NOUN PHRASES ##
def clean_noun_phrases(x): 
    rslt1 = x.replace("[","")
    rslt2 = rslt1.replace("]", "")
    rslt3 = rslt2.replace("'", "")    
    rslt4 = " ".join(rslt3.split())
    return rslt4

    ## GET DOCUMENTS ##
def get_docs():    
    directory = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\preprocessed_NLP_Files'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        df = pd.read_csv(f,encoding='utf-8')   
    
    ## CALL BBOW PHRASE MATCHER ##
    df['new_subtopic'] = df['clean_no_stop_lemmatized'].apply(bbow_phrases)
    ## CALL KEY TERMS ##
    df['key_phrase_raw'] = df['clean_text'].apply(parse_keywords)
    df.to_csv(r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\temp\subtopics_bv1.csv', index=False)
    clean_subtopic() 
    
    
def clean_subtopic():
    df = pd.read_csv(r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\temp\subtopics_bv1.csv', encoding='utf-8')
    
    ## CLEAN BBOW RESULTS ##
    df['subtopic_words'] = df['new_subtopic'].apply(clean_bbow_results)
    
    ## CLEAN KEY TERM RESULTS ##
    df['key_phrase'] = df['key_phrase_raw'].apply(clean_keyterm_results)
    
    ## CLEAN NOUN PHRASES ##
    df['noun_phrases'] = df['noun_phrase'].apply(clean_noun_phrases)
    
    ## CONVERT DATE TO DATETIME
    df['datetime'] = pd.to_datetime(df['parsed_date'], format='mixed')
    ## MAKE ONE HOT ENCODED ##
    #g = pdget_dummies(pd.Series(df.clean_no_stop_lemmatized.str.split('\s').explode())).reindex(columns=[big_bag_of_words]).fillna(0).astype(int)pd.DataFrame(df.iloc[:,0]).join(g.groupby(level=0).sum(0))
     
    # make dummies from subtopics
    df.drop(columns=['keywords','new_subtopic', 'key_phrase_raw','noun_phrase',], axis=1, inplace=True)
    df2 = df.subtopic_words.str.get_dummies(sep=' , ')
    df3 = pd.concat([df, df2], axis=1)  
    df3.to_csv(r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\temp2\model_results_clean_bv1.csv', index=False)
    add_missing_columns()
    
    
# add column padding zeros
def add_zeros(x):
    for i in range(x):
        z = 0
        return z
  
def add_missing_columns():
    timestr = time.strftime("%Y%m%d_%H%M%S")
    df = pd.read_csv(r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\temp2\model_results_clean_bv1.csv', encoding='utf-8')
    big_bag_of_words2 = ['diplomatic', 'abduct', 'abduction', 'abomination', 'abuse', 'account', 'accuse', 'acls', 
             'acquire', 'activism', 'actor', 'actress', 'advancement', 'agree', 'agreement', 'ai', 'aid worker',
             'air', 'air force', 'air strike', 'aircraft carrier', 'album', 'ambassador', 'ambulance', 
             'ammunition', 'anger', 'angry', 'animal', 'antisemitism', 'archaeologist', 'argue', 'argument',
             'army', 'arrest', 'artificial intelligence', 'ash', 'assault', 'assert', 'asteroid', 'astronaut', 
             'athletic', 'atrocity', 'attack', 'auto', 'automobile', 'automotive', 'avalanche', 'avow', 
             'bank bank', 'banking', 'baseball', 'basketball', 'bass', 'bassist', 'battle', 'beaufort scale', 
             'bed and breakfast', 'behead', 'bipartisan', 'bird', 'bird flu', 'black jack', 'blackmail', 
             'blackout', 'blizzard', 'blood supply', 'bloodshed', 'bnb', 'bowl', 'bribe', 'bronze metal', 
             'brutality', 'burglary', 'business', 'business model', 'business strategy', 'campaign', 'campus',
             'cancer', 'carbon emission', 'casualty', 'casualty of war', 'cat', 'ceasefire', 'ceo', 
             'championship', 'chemical', 'chemical warfare', 'cinematic', 'claim', 'clarinet', 'class of', 
             'classroom', 'clean energy', 'climate change', 'cocaine', 'cold', 'college', 'colonel', 'combat',
             'competition', 'competitive analysis', 'computer hacker', 'concert', 'conflict', 
             'conflict resolution', 'conflict zone', 'congress', 'consult', 'contend', 'convict', 'cop', 'corn', 
             'corporate', 'corruption', 'counter attack', 'court rulling', 'covid', 'cow', 'cpu', 'crack', 'crime',
             'criminal investigation', 'criminal offence', 'criminal procedure', 'criminal profiling', 'crisis',
             'crop', 'curriculum', 'customer service', 'cybercrime', 'damage', 'dart', 'dead', 'death', 
             'debate', 'decease', 'defeat', 'defense', 'demise', 'democrats', 'depart', 'destination wedding',
             'detective', 'diabetes', 'diagnose', 'diagnosis', 'digital marketing', 'dinosaur', 'disability',
             'disagree', 'disaster', 'disaster preparedness', 'disaster risk reduction', 'discuss', 'discussion',
             'disease', 'dispute', 'distance learning', 'doctor', 'dog', 'domestic violence', 'drone',
             'drone air strike', 'drought', 'drug', 'drug addiction', 'drug offense', 'drug trafficking', 
             'drummer', 'duck', 'e commerce', 'e learn', 'early childhood education', 'earth', 'economic',
             'education', 'el nina', 'el nino', 'elderly', 'election', 'electric vehicle', 'electrocution',
             'elementary school', 'embezzle', 'embezzlement', 'emergency', 'emergency room', 'emotion',
             'energy', 'entertainment', 'entrepreneurial', 'environment', 'er', 'eruption', 'escalate',
             'escalation of violence', 'espionage', 'espn', 'evacuate', 'evacuation', 'evidence', 
             'exploration', 'explosion', 'export', 'expostulate', 'extort', 'extortion', 'fall', 'farm',
             'fatal', 'fatal shooting', 'fault', 'fbi', 'felony', 'feud', 'fight', 'film', 'finance', 'fire',
             'first aid', 'first place', 'flank', 'flood', 'flu', 'flu season', 'flu shoot', 'fly', 'food',
             'food aid', 'food supply', 'football', 'forecast', 'forensic', 'fraud', 'freedom', 'freeze',
             'frontline', 'fuel', 'game', 'gang war', 'gas', 'gas mask', 'gas price', 'general', 'genocide',
             'global trade', 'global warming', 'gold medalist', 'golf', 'gorilla warfare', 'gpa', 'gpt',
             'grade', 'graduate', 'graduation', 'ground operation', 'guerilla warfare', 'guilty', 'guitar', 
             'guitarist', 'hacker', 'hate crime', 'health', 'health care', 'healthcare record', 'heat', 
             'heat wave', 'heavy rain', 'heinous act', 'heist', 'high education', 'high pressure', 'high rate',
             'highjack', 'hippa', 'hockey', 'hog', 'hold captive', 'hollywood', 'homicide', 'horse', 'hospital',
             'hostage', 'housing market', 'human resource', 'human trafficking', 'humanitarian aid', 'hurricane',
             'ide', 'identity theft', 'ill', 'illegal', 'illness', 'impersonate', 'import export',
             'importation', 'imprisonment', 'industrial', 'industry', 'infanticide', 'inhumane', 
             'injure', 'innovation', 'insect', 'insist', 'insurance fraud', 'insurgent', 'intellectual property',
             'interception', 'internally displace person', 'introduce bill', 'introduce new bill', 
             'investigate', 'investigation', 'investment', 'jail', 'jet', 'judicial', 'juvenile delinquent',
             'kidnap', 'kidney', 'kill', 'killer', 'labor market', 'lake', 'landslide', 'language model',
             'larceny', 'last place', 'launch an attack', 'law', 'law enforcement', 'leadership', 'legal',
             'legal system', 'legislature', 'life imprisonment', 'lifelong learning', 'lightning', 'literacy',
             'low rate', 'lsd', 'machine learning', 'mafia', 'malefaction', 'manufacturing', 'marijuana',
             'marine', 'market research', 'marketing', 'md', 'mediate', 'medical assistance', 'medical board',
             'medical help', 'medical record', 'medication', 'merger', 'meteor', 'militant', 'military', 
             'misdemeanor', 'missile', 'ml', 'mobilization', 'money laundering', 'mortgage', 'movie', 
             'movie star', 'murder', 'music', 'music video', 'musician', 'narcotic', 'nasa', 'nascar',
             'nato', 'navy', 'negotiate', 'new release', 'new technology', 'nlp', 'nuclear',
             'nuclear warfare', 'nuclear weapon', 'numeracy', 'nurse', 'nurse aid', 'nursing', 
             'nursing home', 'ocean', 'offence', 'offender', 'offense', 'officer', 'oil', 'olimpics',
             'olympic', 'online education', 'opera', 'operate', 'operation', 'optical', 'order', 
             'organize crime', 'outer space', 'overtake', 'oxycontin', 'pandemic', 'paramedic', 
             'pass away', 'peace', 'peace corps', 'peace negotiation', 'peacekeeping', 'peacetime negotiation',
             'pedagogy', 'perish', 'perpetrator', 'piano', 'pig', 'ping pong', 'pitch', 
             'plaintiff', 'plane', 'planet', 'plead', 'plumet', 'poker', 'police', 'pollute', 
             'pollution', 'pool', 'post conflict', 'pow', 'power lifting', 'prescription', 'price increase', 
             'price soar', 'price thrive', 'prison', 'prisoner of war', 'produce', 'project management',
             'prostitution', 'punishable', 'punishment', 'punitive damage', 'quarrel', 'race', 'racketeering',
             'radioactive', 'rain', 'ransom', 'rape', 'real estate', 'record', 'red cross', 'refugee',
             'rehabilitation', 'relief', 'renewable energy', 'republican', 'restaurant', 'retail', 'revenue',
             'rise', 'risk management', 'rivalry', 'robbery', 'sale', 'sanitation', 'satellite', 'school',
             'scientist', 'second place', 'secondary education', 'security', 'sentence', 'sergeant', 
             'serial killer', 'series', 'setback', 'sex offence', 'sexual', 'sexual violence', 
             'sexually assault', 'shelter', 'shoot', 'shoot out', 'shotput', 'shuttle', 'sick',
             'sickness', 'side effect', 'silver metal', 'singer', 'sirus', 'slain', 'slay', 
             'small business', 'smoke', 'snow', 'soccer', 'solar', 'solder', 'song', 'space',
             'spacecraft', 'sport medicine', 'sport medium', 'squabble', 'startup', 'state', 
             'state of the art', 'statutory', 'steal', 'stock market', 'stock price', 'strike', 
             'student', 'submarine', 'succession', 'summer sport', 'supply chain', 'surgeon',
             'surgeon general', 'surgery', 'surrender', 'suspect', 'sustainability', 
             'sustainable development', 'tactic', 'tank', 'teaching', 'technology', 'rebel',
             'technology count', 'tennis', 'tension', 'tension rise', 'terminal ill', 
             'terrorism', 'terrorist activity', 'terrorist activityfood and water', 'terrorist group', 
             'theft', 'thief', 'third place', 'tornado', 'touchdown', 'trade', 'tragedy', 'trans gender', 
             'transgression', 'travel', 'treatment', 'trend', 'troop', 'tsunami', 'tv', 'unemployment',
             'uniform', 'universe', 'unlawful', 'unlivable condition', 'upset', 'us space force', 
             'usaid', 'vacation', 'vaccination', 'vaccine', 'vagrancy', 'vandalism', 'vegetation', 
             'veteran', 'victim', 'victory', 'video game', 'violence', 'violent protest', 'virus',
             'volcano', 'voter', 'vulnerable population', 'war', 'war crime', 'wartime', 'water', 
             'water level', 'weapon', 'weapon of mass destruction', 'weather', 'weight lifting', 
             'whale', 'white collar crime', 'white out', 'wild life', 'wildfire', 'win', 'wind', 
             'windstorm', 'winter sport', 'witness', 'witness protection', 'x ray']
    
    # get leingth of current df
    cols = []
    rows = len(df.index)
    
    # if columns in df not in bbow list, then add them to cols list
    for i in big_bag_of_words2:
        if i not in (df.columns):
            cols.append(i)
            
     # make dict from list as keys and assign 0
    d = dict.fromkeys(cols)
    
    #d = dict(zip(cols, values))
    df2 = pd.DataFrame.from_dict([d])
    
    # join columns to original df
    df3 = pd.concat([df, df2], ignore_index=True)  
    
    # add zeros to df where new columns have been added.
    for newcol in cols:
        df3[newcol] = df3[newcol].apply(lambda x: add_zeros(rows))
        
    df3.to_csv(Fr'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\pre_out\NLP_subtopic_bv1_{timestr}.csv', index=False)    

def separate_countries(): 
    timestr = time.strftime("%Y%m%d_%H%M%S")    
    directory = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\pre_out'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        df = pd.read_csv(f,encoding='utf-8')      
    df['gpe'] = df['gpe'].str.split(',')
    df2 = df.explode('gpe')
    df2.to_csv(Fr'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\out_by_country\NLP_by_country_bv1_{timestr}.csv', index=False)

def get_iso_codes():   
    timestr = time.strftime("%Y%m%d_%H%M%S")    
    directory = r'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\out_by_country'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        df = pd.read_csv(f,encoding='utf-8')   
    
    # all functions here from my import method from iso_codes_bv1.py script
    df['location2'] = df['gpe'].apply(state_to_counrty)
    
    # normalize country names
    df['location'] = df['location2'].apply(country_name)
    
    # get iso3 code
    df['iso3'] = df['location'].apply(get_iso3)
    
    # get lat
    df['lat'] = df['iso3'].apply(get_lat)
    
    # get long
    df['long'] = df['iso3'].apply(get_long)
    
    df.to_csv(Fr'C:\Users\benja\Documents\BTBdataSolutions\BTBdataSolutions\main\out\nlp_country_iso_table_{timestr}.csv', index=False)
    
    
    
###############################################################
def main():
    get_docs()
    clean_subtopic()
    add_missing_columns()
    separate_countries()
    get_iso_codes()
##################### RUN SCRIPT ##############################
if __name__ == "__main__":
    main()

  
