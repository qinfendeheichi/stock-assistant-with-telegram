#!/usr/bin/env python
# coding: utf-8

# In[7]:


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
import random
nlp = spacy.load('en_core_web_sm') 

#global recorder
recorder=[]
#recoreder is used to record all the core messages during the state trasition

punc=[',','.','!','?']

INIT='INIT'
ASK_NORTH_NAME='ASK_NORTH_NAME'
SEND_ERROR_='SEND_ERROR_'
SEND_TIME_ERROR_='SEND_TIME_ERROR_'
ASK_TIME='ASK_TIME'
ASK_ATTRIBUTE='ASK_ATTRIBUTE'
ASK_DAYS='ASK_DAYS'
INTRO_='INTRO_'
SHOW_NORTH_='SHOW_NORTH_'
SHOW_BASIC_='SHOW_BASIC_'
SHOW_RATING_='SHOW_RATING_'
ASK_ATTRIBUTE_NAME='ASK_ATTRIBUTE_NAME'
ASK_BOTTOM_NAME='ASK_BOTTOM_NAME'
SHOW_BOTTOM_='SHOW_BOTTOM_'
SHOW_MORNING_RATIO_='SHOW_MORNING_RATIO_'
ASK_MORNING_NAME='ASK_MORNING_NAME'
SEND_THANKS_='SEND_THANKS_'
SEND_SORRY_='SEND_SORRY_'
SHOW_ACC_='SHOW_ACC_'
month_match={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'july':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
recorder=[]


# In[11]:


class word:
    def sorry():
        return random.choice(["I'm sorry!","Sorry,","Forgive me,","Please,"])
    def n():
        return random.choice(["do not","can not","fail to","could not"])
    def get():
        return random.choice(["understand","get","retrieve"])
    def the_your():
        return random.choice(["the","your"])
    def target():
        return random.choice(["message","intent","meaning","point"])
    def punc():
        return random.choice(['!','.'])
    def filling():
        return random.choice(['Em, ','Then,','I got it, ','Hey, ','Hi, ','','Yep,','Opps','And,'])
    def modal_verb():
        return random.choice(['Can','Could'])
    def ask():
        return random.choice(['let me know','tell me','give me'])
    def name():
        return random.choice(['the name','the code'])
    def target():
        return random.choice(['the security','the stock','your target','your security','your target'])
    def time():
        return random.choice(['the time','the exact time','the specific time or period'])
    def duration():
        return random.choice(['for how many days','for how long','for how much time'])
    def continuous():
        return random.choice(['continuously','constantly'])
    def passive_buy():
        return random.choice(['bought','purchased','gained','held'])
    def wait():
        return random.choice(['wait a minute','wait a second','give me some time','give me some seconds'])
    def alleviate():
        return random.choice(["Don't worry!","Please,","Be patient!"])
    def imporve_modal_verb():
        return random.choice(["may",'will','can'])
    def improve_verb():
        return random.choice(['improve my self','be better','make a difference','make progress'])
    


# In[12]:


def case_init():                            # STATE INIT
    return 'welcome back!'

def case_ask_north_name():                  # STATE ASK_NORTH_NAME    
    return word.filling()+" "+word.modal_verb()+" "+"you "+word.ask()+" "+word.name()+" of "+word.target()+"?"

def case_send_error_():  
    return word.sorry()+" "+"I "+word.n()+" "+word.get()+" "+word.the_your()+" "+word.target()+word.punc()


def case_send_time_error_():                          # STATE case_send_error_
    """
    to be updated in the future
    """
    return case_send_error_()

def case_ask_time():                            # STATE ASK_TIME
    return word.filling()+" "+word.modal_verb()+" you "+word.ask()+" "+word.time()+" ?"

def case_ask_attribute():                            # STATE_ASK_ATTRIBUTE
    return "about what attribute? volume or price?"

def case_ask_days():                            # STATE ASK_DAYS
    return word.filling()+" "+word.duration()+" do you want to "+word.get()+" the info about "+"the north-oriented money that " +word.continuous()+" "+word.passive_buy()+" "+ word.target()+" ?"

def case_intro_():            
    return 'I am your personal sweetie stock info robot'

def case_show_north_():                            
    return word.alleviate()+" "+word.wait()+" "+word.punc()

def case_show_basic_():                  
    return word.alleviate()+" "+word.wait()+" "+word.punc()

def case_show_rating_():                  
    return word.alleviate()+" "+word.wait()+" "+word.punc()

def case_ask_attribute_name():                     
    return word.filling()+" "+word.modal_verb()+" you "+word.ask()+" "+word.name()+" ?"

def case_ask_bottom_name():                          
    return word.filling()+" "+word.modal_verb()+" you "+word.ask()+" "+word.name()+" ?"

def case_show_bottom_():                        
    return word.alleviate()+" "+word.wait()+" "+word.punc()

def case_show_morning_ratio_():                  
    return word.alleviate()+" "+word.wait()+" "+word.punc()

def case_ask_morning_name_():                
    return word.filling()+" "+word.modal_verb()+" you "+word.ask()+" "+word.name()+" ?"

def case_send_thanks_():                         
    return "I am pretty happy now!"

def case_send_sorry_():                        
    return word.sorry()+" "+"I "+word.improve_modal_verb()+" "+word.improve_verb()+" in the future"+word.punc()

def case_show_acc_():                
    return word.filling()+" "+word.modal_verb()+" you "+word.ask()+" "+word.name()+" ?"

def default():
    return '...'

# reply word materials

switch_word = {'INIT': case_init,             
          'ASK_NORTH_NAME': case_ask_north_name,
          'SEND_ERROR_': case_send_error_,
          'SEND_TIME_ERROR_': case_send_time_error_,
          'ASK_TIME': case_ask_time,
          'ASK_ATTRIBUTE': case_ask_attribute,
          'ASK_DAYS': case_ask_days,
          'INTRO_': case_intro_,
          'SHOW_NORTH_': case_show_north_,
          'SHOW_BASIC_': case_show_basic_,
          'SHOW_RATING': case_show_rating_,
          'ASK_ATTRIBUTE_NAME': case_ask_attribute_name,
          'ASK_BOTTOM_NAME': case_ask_bottom_name,
          'SHOW_BOTTOM_': case_show_bottom_,
          'SHOW_MORNING_RATIO_': case_show_morning_ratio_,
          'ASK_MORNING_NAME_': case_ask_morning_name_,
          'SEND_THANKS_': case_send_thanks_,
          'SEND_SORRY_': case_send_sorry_,
          'SHOW_ACC_': case_show_acc_,
          }


# In[9]:


def image_show_north_():
    return show_north_

def image_show_basic_():
    return show_basic_

def image_show_bottom_():
    return show_bottom_

def image_show_morning_ratio_():
    return show_morning_ratio_

def image_show_acc_():
    return show_acc_

def no_image_(state,recorder):
    return None

def default_image_():
    return no_image_


switch_image={ 
            'SHOW_NORTH_': image_show_north_,
          'SHOW_BASIC_': image_show_basic_ ,
    'SHOW_MORNING_RATIO_':image_show_morning_ratio_,
    'SHOW_ACC_':image_show_acc_,
    'SHOW_BOTTOM_':image_show_bottom_
    #     'SHOW_MORNING_RATIO':image_show_ratio,
#     'SHOW_ACC':image_show_acc_
}

