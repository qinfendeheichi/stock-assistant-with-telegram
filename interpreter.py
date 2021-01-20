#!/usr/bin/env python
# coding: utf-8

import re
import spacy
import datetime
from textblob import TextBlob
from send_receive import *
import time
import pandas as pd
import numpy as np
from policy import *
from show_north_ import *
from show_acc_ import *
from show_basic_ import *
from show_morning_ratio_ import *
from show_bottom_ import *
from text_rating_ import *
from initialize import *
from interpreter import *
nlp = spacy.load('en_core_web_sm') 
month_match={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'july':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
punc=[',','.','!','?']

def interpret(message):
    msg = message.lower()
    '''
    'ask_intro'                ## 'who','you do','intro'                                    o
    'north_analysis'           ##'north'
    'name'                     ## 6-digt integer                                     
    'name_attribute'           ## combined
    'basic_attribute'          ## 'volume','price' 
    'non_latest_time'          # 
    'rating'                   ## 'rate','rating','evaluat','apprais'
    'period'                   #period
    'north_buy_much_name'      ## 'north'+'cons'/'days'+'name'
    'number'                   ## 1/2-digit integer
    'north_buy_much_number_name'## 'north' +'con'/'days' + /s1/2-digit integer/s+'name'
    'double_bottom'            ## 'bottom'
    'double_bottom_name'       ## 'bottom' + 6-digt integer 
    'morning_ratio_name'       ## 'mor'+'pro'/'sca'/per/ratio+ 6-digt integer
    'morning_ratio'            ## 'mor'+'pro'/'sca'/per/ratio
    
    'compliment'             # sentiment analysis powered by textblob
    'criticism'
    'other'
    '''
    
    has_name=False
    has_north=False
    has_attribute=False
    has_non_latest_day=False      #if has_non_latest_time is true, then has_period is true also.
    has_rating=False
    has_period=False
    has_consecutive=False
    has_number=False
    has_bottom=False
    has_morning=False
    
    name_value=None
    attribute_value=None
    date_value=None
    period_value=None
    number_value=None

    
    temp=msg
    if re.search(r'[.]*\d{6}[.]*', temp)!=None:
        index=re.search(r'[.]*\d{6}[.]*', temp).span()
        name_value=temp[index[0]:index[1]]
        has_name=True
    if re.search(r'[.]*north[.]*',temp)!=None:
        has_north=True
    if re.search(r'[.]*volume|price[.]*',temp)!=None:
        has_attribute=True
        index=re.search(r'[.]*volume|price[.]*', temp).span()
        attribute_value=temp[index[0]:index[1]]
        if attribute_value[-1] in punc:
            attribute_value=attribute_value[:-1]
    if re.search(r'[.]*\s\d\s[.]*',temp)!=None:
        has_number=True
        index=re.search(r'[.]*\s\d\s[.]*', temp).span()
        number_value=int(temp[index[0]:index[1]])
    if re.search(r'[.]*con|conti|constant|freq[.]*',temp)!=None:
        has_consecutive=True
    if re.search(r'[.]*mor[.]*',temp)!=None and re.search(r'[.]*ratio|per|ratio|pro|scal[.]*',temp)!=None:
        has_morning=True
    if re.search(r'[.]*rat|evaluat|apprai[.]*',temp)!=None:     
        has_rating=True     
    if re.search(r'[.]*bottom[.]*',temp)!=None:     
        has_bottom=True


    doc=nlp(temp)
    count=0
    start_date=None
    end_date=None   #if it is only a date, end_date is None, else, it is a period when both start_date and end_date are not None

    for ent in doc.ents:
    #     print(ent.text, ent.label_)
        if ent.label_=='DATE':
            if re.match(r'[.]*\d{6}[.]*', ent.text):
                continue
            else:

                temp1=re.findall('feb|mar|jan|apr|may|jun|july|aug|sep|oct|nov|dec|\d|\d\d',temp)
                if temp1==[]:
                    continue
                else:
                    if len(temp1)==2:
                        month=month_match[temp1[0]]
                        day=temp1[1]
                        if start_date==None:
                            start_date=datetime.date(2020,int(month),int(day))
                        else:
                            end_date=datetime.date(2020,int(month),int(day))
                            has_period=True
                    if len(temp1)==4:
                        
                        month=month_match[temp1[0]]
                        day=temp1[1]
                        start_date=datetime.date(2020,int(month),int(day))
                        month=month_match[temp1[2]]
                        day=temp1[3]
                        end_date=datetime.date(2020,int(month),int(day))  
                        has_period=True
                    has_non_latest_day=True
    if has_period==True:
        period_value=(start_date,end_date)
        return 'period',period_value
        
    else:
        if has_non_latest_day==True:
            date_value=start_date
            if date_value!=None:
                return 'non_latest_time',date_value
        
    if re.search(r'[.]*who|you\sdo|can\syou|intro[.]*', temp)!=None:
        return 'ask_intro',None
    
    if has_north==True and has_consecutive==True and has_name==True and has_number==True:
        return 'north_buy_much_number_name',(number_value,name_value)

    if has_north==True and has_consecutive==True and has_name==True  :
        return 'north_buy_much_name',name_value
    
    if has_morning==True and has_name==True:
        return 'morning_ratio_name',name_value
    
    if has_morning==True:
        return 'morning_ratio',None
    
    if has_bottom==True and has_name==True:
        return 'double_bottom_name',name_value
    
    if has_bottom==True:
        return 'double_bottom',None
    
    if has_name==True and has_attribute==True:
        return 'name_attribute',(name_value,attribute_value)

    if has_rating==True:

        return 'rating',None
    
    if has_attribute==True:
        return 'basic_attribute',attribute_value
    
    if has_north==True:
        return 'north_analysis',None
    
    if has_name==True:
        return 'name',name_value
    
    if has_number==True:
        return 'number',number_value  
    
    text = '''you did a good job. I really really hate you. how bad you are. you are so stupid, my bot'''
    blob = TextBlob(temp)
    for sentence in blob.sentences:
        if sentence.sentiment.polarity>0.5:
            return 'compliment',None
        if sentence.sentiment.polarity<-0.5:
            return 'criticism',None
    return 'other',None

