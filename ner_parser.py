# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:51:36 2023

@author: BTB Data Solutions, Ben Bergenstein

NLP Text Preprocessing and NER parser.
"""
import spacy
import pandas as pd
import os
import time
import datetime
# keeping 9 entities

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
    black_list = ["LANGUAGE", "DATE", "TIME", "PERCENT", "QUANTITY", "ORDINAL", "MONEY","CARDINAL", "WORK_OF_ART"]
    nlp = spacy.load('en_core_web_md')     
    doc = nlp(data)
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
        else:
            pass
    peopleb = list(set(people))
    norpb = list(set(norp))
    norpb = list(set(norp))
    facb = list(set(fac))
    orgb = list(set(org))
    gpeb = list(set(gpe))
    locb = list(set(loc))
    productb = list(set(product))
    eventb = list(set(event))
    
    print(peopleb)
    return peopleb, norpb, facb,orgb, gpeb, locb, productb,eventb
    

def read_in_docs_NER():
    # dir of files to process
    directory = r'C:\Users\benja\OneDrive\Documents\BTBdataSolutions_Project\test_data'    
    # iterate over files in directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")        
        file_name = timestr + '.csv'  
        df = pd.read_csv(f,encoding='utf-8')  
        # merge 2 cols into 1 col
        df['text_merged'] = df[['title', 'text']].apply(lambda x: ' '.join(x), axis=1)
        # join multiple lists into separate cols
        df["people"],df["norp"],df["fac"],df["org"],df["gpe"],df["loc"],df["product"],df["event"] = zip(*df["text_merged"].map(ner_extraction))
                
        df.to_csv(Fr'C:\Users\benja\OneDrive\Documents\BTBdataSolutions_Project\ner_out_temp\{file_name}', index=False)
           
def clean_ner():
    directory = r'C:\Users\benja\OneDrive\Documents\BTBdataSolutions_Project\ner_out_temp'  
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
    
        df.to_csv(Fr'C:\Users\benja\OneDrive\Documents\BTBdataSolutions_Project\ner_out\{filename}', index=False)

def main():
    read_in_docs_NER() 
    clean_ner()
    

#####################RUN SCRIPT ##############################
if __name__ == "__main__":
    main()
    
