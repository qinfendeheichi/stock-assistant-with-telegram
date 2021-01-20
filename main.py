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

def send_message(state, message,user_id):
    new_state, response = respond(state, message)
    send_text(user_id,response)
    image_location=reply_image(new_state,recorder)
    if image_location!=None:
        send_picture(user_id,{'photo': open(image_location, 'rb')})
    if new_state=='SHOW_RATING_':
        response=text_rating_(new_state,recorder)
        send_text(user_id,response)
    return new_state

def respond(state, message):
    intent,content=interpret(message)
    if content!=None:
        if isinstance(content,tuple):
            for i in content:
                recorder.append(i)
        else:
            recorder.append(content)
    new_state=policy_rules.loc[state,intent]
    response=reply_word(new_state,recorder)
    return new_state,response

def reply_word(state,recorder):
    choice = state
    
    #two kinds of situations enter the state "SHOW_NORTH_"
    if state=="SHOW_NORTH_" and len(recorder)==1:
        return "Don't worry! I will show you the result!"
    
    return switch_word.get(choice, default)()       

def reply_image(state,recorder):
    choice = state 
    return switch_image.get(choice, default_image_)()(state,recorder)  

recorder=[]
old_message=None
state=INIT
while(1):
    user_id, type,message=get_my_info()
    if message==old_message:
        continue
    old_message=message
    print(state)
    state=send_message(state,message,user_id)
    if state[-1]=='_':
        state=INIT
        recorder=[]



