# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:28:54 2024

@author: BTB
"""

import spacy
import textacy 
from spacy.matcher import PhraseMatcher
import pandas as pd
import re
nlp = spacy.load("en_core_web_md")
matcher = PhraseMatcher(nlp.vocab)
def bbow_phrases(x):
    
    ## BBOW PHRASE MATCHER ##
    big_bag_of_words = ['sale', 'basketball', 'lifelong learning', 'tragedy', 'finance', 'hostage', 'argument',
                        'diabetes', 'import export', 'nurse aid', 'pedagogy', 'mediate', 'prostitution', 
                        'tsunami', 'computer hacker', 'outer space', 'malefaction', 'narcotic',
                        'emergency', 'drug offense', 'plaintiff', 'farm', 'white out', 'universe',
                        'consult', 'win', 'ide', 'mafia', 'legislature', 'nasa', 'peace corps', 
                        'marijuana', 'violence', 'ceasefire', 'anger', 'water', 'flu', 'elderly',
                        'antisemitism', 'trade', 'e learn', 'plead', 'freeze', 'new technology', 
                        'colonel', 'offence', 'blackmail', 'doctor', 'theft', 'peacekeeping', 'oil',
                        'heinous act', 'md', 'technology', 'business', 'piano', 'legal', 'high education',
                        'larceny', 'counter attack', 'victim', 'embezzle', 'law enforcement', 
                        'casualty of war', 'jet', 'veteran', 'industrial', 'squabble', 'homicide', 
                        'air strike', 'burglary', 'online education', 'stock market', 'tornado',
                        'activism', 'export', 'troop', 'chemical warfare', 'discuss', 
                        'intellectual property', 'disaster risk reduction', 'operation',
                        'silver metal', 'nato', 'red cross', 'meteor', 'satellite', 'small business',
                        'statutory', 'cpu', 'guilty', 'winter sport', 'heat wave', 'nascar',
                        'human resource', 'innovation', 'insist', 'chemical', 'officer', 'prescription',
                        'criminal investigation', 'conflict zone', 'second place', 'highjack', 'earth',
                        'pool', 'offense', 'kill', 'bipartisan', 'olimpics', 'hockey', 'shuttle',
                        'electrocution', 'misdemeanor', 'gas mask', 'blackout', 'ammunition', 'heist',
                        'lake', 'video game', 'duck', 'thief', 'upset', 'punitive damage', 'athletic',
                        'heavy rain', 'automobile', 'dead', 'illness', 'felony', 'gas', 'health', 
                        'radioactive', 'clean energy', 'setback', 'space', 'diagnosis', 'guitarist',
                        'inhumane', 'military', 'genocide', 'cocaine', 'weather', 'slain',
                        'witness protection', 'fatal shooting', 'soccer', 'insect', 'bribe', 'attack',
                        'business model', 'terrorism', 'weapon', 'ransom', 'climate change', 'abduction',
                        'merger', 'nuclear warfare', 'election', 'student', 'sport medicine', 'state',
                        'illegal', 'beaufort scale', 'poker', 'casualty', 'price soar', 
                        'risk management', 'windstorm', 'cinematic', 'wind', 'assert', 'manufacturing',
                        'feud', 'ml', 'arrest', 'energy', 'global warming', 'defeat', 'food', 'drone',
                        'peacetime negotiation', 'competition', 'travel', 'vagrancy', 'medical record',
                        'food aid', 'expostulate', 'blood supply', 'court rulling', 'movie', 'last place',
                        'global trade', 'whale', 'escalation of violence', 'discussion', 'quarrel', 
                        'combat', 'customer service', 'mortgage', 'grade', 'hurricane', 'nurse', 
                        'aid worker', 'cold', 'flood', 'conflict', 'movie star', 'jail', 'surrender',
                        'disaster', 'defense', 'tension', 'offender', 'uniform', 'avow', 'robbery', 
                        'post conflict', 'rivalry', 'album', 'animal', 'food supply', 'water level',
                        'evacuate', 'technology count', 'launch an attack', 'gang war', 'diagnose', 
                        'injure', 'medication', 'pass away', 'rape', 'bird', 'introduce bill', 'football',
                        'dispute', 'marine', 'e commerce', 'criminal procedure', 'spacecraft',
                        'domestic violence', 'drug trafficking', 'mobilization', 'bnb', 'usaid', 'air', 
                        'criminal profiling', 'fly', 'guitar', 'optical', 'game', 'drug addiction',
                        'drummer', 'bed and breakfast', 'sirus', 'landslide', 'leadership', 'tactic', 
                        'relief', 'navy', 'graduation', 'acquire', 'nuclear', 'numeracy', 
                        'white collar crime', 'archaeologist', 'suspect', 'health care', 'sickness', 
                        'business strategy', 'hippa', 'hospital', 'punishable', 'smoke', 'espn', 
                        'war crime', 'decease', 'judicial', 'tank', 'cancer', 'disagree', 'restaurant',
                        'black jack', 'detective', 'horse', 'fire', 'distance learning', 'ping pong',
                        'eruption', 'unemployment', 'peace', 'sport medium', 'damage', 'wild life',
                        'emergency room', 'crop', 'series', 'war', 'overtake', 'retail', 'hollywood', 
                        'dog', 'terrorist group', 'ai', 'volcano', 'account', 'gas price', 'strike', 
                        'record', 'gold medalist', 'solar', 'racketeering', 'music video', 'death', 
                        'actress', 'shotput', 'fuel', 'disaster preparedness', 'nlp', 'carbon emission',
                        'acls', 'avalanche', 'fatal', 'serial killer', 'vandalism', 'championship', 
                        'astronaut', 'automotive', 'electric vehicle', 'curriculum', 'campaign', 
                        'succession', 'heat', 'sexual violence', 'new release', 'asteroid', 'investment',
                        'bowl', 'abduct', 'supply chain', 'machine learning', 'ocean', 'cat', 
                        'vaccination', 'claim', 'planet', 'wartime', 'bronze metal', 'price thrive',
                        'forensic', 'killer', 'project management', 'housing market', 'weight lifting',
                        'actor', 'brutality', 'militant', 'vaccine', 'fall', 'investigation', 'espionage',
                        'slay', 'power lifting', 'democrats', 'cow', 'life imprisonment', 
                        'drone air strike', 'campus', 'touchdown', 'police', 'sustainable development',
                        'frontline', 'nursing', 'sentence', 'hog', 'insurance fraud', 'ambulance', 'gpa',
                        'voter', 'forecast', 'covid', 'cop', 'bass', 'artificial intelligence', 'extort',
                        'terminal ill', 'ill', 'peace negotiation', 'sustainability', 'tv', 'teaching',
                        'real estate', 'singer', 'nursing home', 'pig', 'infanticide', 'state of the art',
                        'music', 'dinosaur', 'drug', 'impersonate', 'sanitation', 'submarine',
                        'gorilla warfare', 'corporate', 'elementary school', 'vacation', 'scientist', 
                        'fight', 'fbi', 'escalate', 'perish', 'surgery', 'evidence', 'school',
                        'class of', 'high rate', 'produce', 'clarinet', 'pollute', 'language model', 
                        'shelter', 'investigate', 'plumet', 'flank', 'early childhood education',
                        'bird flu', 'song', 'bassist', 'convict', 'operate', 'sexually assault', 
                        'security', 'film', 'sick', 'auto', 'interception', 'secondary education', 
                        'entrepreneurial', 'weapon of mass destruction', 'debate', 'destination wedding',
                        'imprisonment', 'refugee', 'baseball', 'kidnap', 'stock price', 'snow', 
                        'bloodshed', 'sex offence', 'startup', 'er', 'air force', 'digital marketing', 
                        'terrorist activityfood and water', 'x ray', 'transgression', 'market research',
                        'medical assistance', 'battle', 'low rate', 'golf', 'healthcare record', 
                        'congress', 'lightning', 'murder', 'first place', 'prison', 'vulnerable population',
                        'corn', '   diplomatic', 'atrocity', 'general', 'agreement', 'extortion',
                        'crack', 'hold captive', 'missile', 'corruption', 'sergeant', 'crisis', 'graduate',
                        'labor market', 'steal', 'marketing', 'legal system', 'exploration', 'army', 
                        'hacker', 'tension rise', 'gpt', 'dart', 'lsd', 'shoot out', 'juvenile delinquent',
                        'entertainment', 'pitch', 'abuse', 'nuclear weapon', 'side effect', 'rain',
                        'education', 'treatment', 'fraud', 'cybercrime', 'importation', 'kidney', 
                        'trans gender', 'punishment', 'first aid', 'literacy', 'high pressure', 
                        'violent protest', 'freedom', 'witness', 'third place', 'surgeon', 'embezzlement',
                        'perpetrator', 'banking', 'flu shoot', 'race', 'terrorist activity', 'blizzard',
                        'pow', 'bank bank', 'hate crime', 'criminal offence', 'tennis', 
                        'introduce new bill', 'depart', 'price increase', 'solder', 'assault', 'college',
                        'explosion', 'virus', 'drought', 'aircraft carrier', 'plane', 'concert',
                        'advancement', 'accuse', 'unlawful', 'rehabilitation', 'industry', 'crime',
                        'medical board', 'surgeon general', 'identity theft', 'conflict resolution',
                        'environment', 'guerilla warfare', 'disability', 'musician', 'fault', 'opera', 
                        'victory', 'emotion', 'angry', 'flu season', 'ambassador', 'el nina', 'trend', 
                        'prisoner of war', 'olympic', 'renewable energy', 'human trafficking', 
                        'vegetation', 'economic', 'law', 'sexual', 'negotiate', 'oxycontin', 'ceo', 
                        'behead', 'contend', 'order', 'paramedic', 'el nino', 'wildfire', 'insurgent',
                        'abomination', 'agree', 'organize crime', 'internally displace person', 
                        'ground operation', 'humanitarian aid', 'classroom', 'demise', 'republican',
                        'money laundering', 'evacuation', 'disease', 'summer sport', 'argue', 
                        'pollution', 'us space force', 'revenue', 'medical help', 'competitive analysis',
                        'pandemic', 'shoot', 'unlivable condition']
        
    
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
    rslt5 = " ".join(rslt4.split())
    return rslt5
    
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
    df = pd.read_csv(r'C:\BTBdata\nlp_bv1_20231217_194152.csv', encoding='utf-8')
    ## CALL BBOW PHRASE MATCHER ##
    df['new_subtopic'] = df['clean_no_stop_lemmatized'].apply(bbow_phrases)
    
    ## CALL KEY TERMS ##
    df['key_phrase_raw'] = df['clean_text'].apply(parse_keywords)
    df.to_csv(r'BTBdata\subtopics_bv1.csv', index=False)
    clean_subtopic() 
    
    
def clean_subtopic():
    df = pd.read_csv(r'C:\BTBdata\subtopics_bv1.csv', encoding='utf-8')
    
    ## CLEAN BBOW RESULTS ##
    df['subtopic_words'] = df['new_subtopic'].apply(clean_bbow_results)
    
    ## CLEAN KEY TERM RESULTS ##
    df['key_phrase'] = df['key_phrase_raw'].apply(clean_keyterm_results)
    
    ## CLEAN NOUN PHRASES ##
    df['noun_phrases'] = df['noun_phrase'].apply(clean_noun_phrases)
    
    ## CONVERT DATE TO DATETIME
    df['datetime'] = pd.to_datetime(df['parsed_date'], format='mixed')
    ## MAKE ONE HOT ENCODED ##
    # make dummies from subtopics
    #df2 = pd.concat([df, df['new_subtopics'].str.get_dummies(sep=',')], axis=1)
    df.drop(columns=['keywords','new_subtopic', 'key_phrase_raw','noun_phrase',], axis=1, inplace=True)
    
    df.to_csv(r'C:\BTBdata\model_results_bv1.csv', index=False)

  
get_docs()    
