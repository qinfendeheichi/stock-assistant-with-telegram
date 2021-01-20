#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ask_intro=pd.Series({'INIT':'INTRO_',                 'ASK_NORTH_NAME':'INTRO_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'INTRO_',     
           'ASK_DAYS':'INTRO_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'INTRO_',
          'ASK_BOTTOM_NAME':'INTRO_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'INIT',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
          'SHOW_ACC_':'INIT'})

north_analysis=pd.Series({'INIT':'ASK_NORTH_NAME',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SHOW_NORTH_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'INIT',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                         'SHOW_ACC_':'INIT'})

name=pd.Series({'INIT':'ASK_ATTRIBUTE',                 'ASK_NORTH_NAME':'SHOW_NORTH_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SHOW_BASIC_',
          'ASK_BOTTOM_NAME':'SHOW_BOTTOM_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SHOW_MORNING_RATIO_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
               'SHOW_ACC_':'INIT'})

name_attribute=pd.Series({'INIT':'SHOW_BASIC_',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SHOW_BASIC_',
          'ASK_BOTTOM_NAME':'SHOW_BOTTOM_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SHOW_MORNING_RATIO_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                         'SHOW_ACC_':'INIT'})

basic_attribute=pd.Series({'INIT':'ASK_ATTRIBUTE_NAME',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SHOW_BASIC_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SHOW_BASIC_',
          'ASK_BOTTOM_NAME':'SHOW_BOTTOM_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SHOW_MORNING_RATIO_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                         'SHOW_ACC_':'INIT'})

non_latest_time=pd.Series({'INIT':'SEND_TIME_ERROR_',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SHOW_RATING_',    'ASK_ATTRIBUTE':'SEND_TIME_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SHOW_BASIC_',
          'ASK_BOTTOM_NAME':'SHOW_BOTTOM_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SHOW_MORNING_RATIO_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                          'SHOW_ACC_':'INIT'})

rating=pd.Series({'INIT':'ASK_TIME',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                 'SHOW_ACC_':'INIT'})

period=pd.Series({'INIT':'SEND_TIME_ERROR_',                 'ASK_NORTH_NAME':'SEND_TIME_ERROR_',    'SENDERROR_':'SEND_TIME_ERROR_',
           'SEND_TIME_ERROR_':'SEND_TIME_ERROR_',      'ASK_TIME':'SHOW_RATING_',    'ASK_ATTRIBUTE':'SEND_TIME_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                  'SHOW_ACC_':'INIT'})

north_buy_much_name=pd.Series({'INIT':'ASK_DAYS',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'SEND_ERROR_',
           'SEND_TIME_ERROR_':'SEND_ERROR_',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                              'SHOW_ACC_':'INIT'})

#未完待续+show_acc
number=pd.Series({'INIT':'SEND_ERROR_',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'SEND_ERROR_',
           'SEND_TIME_ERROR_':'SEND_ERROR_',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SHOW_ACC_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                 'SHOW_ACC_':'INIT'})

north_buy_much_number_name=pd.Series({'INIT':'SHOW_ACC_',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'SEND_ERROR_',
           'SEND_TIME_ERROR_':'SEND_ERROR_',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                 'SHOW_ACC_':'INIT'})

double_bottom=pd.Series({'INIT':'ASK_BOTTOM_NAME',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'SEND_ERROR_',
           'SEND_TIME_ERROR_':'SEND_ERROR_',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                 'SHOW_ACC_':'INIT'})

double_bottom_name=pd.Series({'INIT':'SHOW_BOTTOM_',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                 'SHOW_ACC_':'INIT'})

morning_ratio_name=pd.Series({'INIT':'SHOW_MORNING_RATIO_',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                 'SHOW_ACC_':'INIT'})
morning_ratio=pd.Series({'INIT':'ASK_MORNING_NAME',                 'ASK_NORTH_NAME':'SEND_ERROR_',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'SEND_ERROR_',    'ASK_ATTRIBUTE':'SEND_ERROR_',     
           'ASK_DAYS':'SEND_ERROR_',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'SEND_ERROR_',
          'ASK_BOTTOM_NAME':'SEND_ERROR_',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'SEND_ERROR_',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                 'SHOW_ACC_':'INIT'})

compliment=pd.Series({'INIT':'SEND_THANKS_',                 'ASK_NORTH_NAME':'SEND_THANKS_',    'SENDERROR_':'SEND_THANKS_',
           'SEND_TIME_ERROR_':'SEND_THANKS_',      'ASK_TIME':'SEND_THANKS_',    'ASK_ATTRIBUTE':'SEND_THANKS_',     
           'ASK_DAYS':'SEND_THANKS_',             'INTRO_':'SEND_THANKS_',              'SHOW_NORTH_':'SEND_THANKS_',        
           'SHOW_BASIC_':'SEND_THANKS_',            'SHOW_RATING_':'SEND_THANKS_',        'ASK_ATTRIBUTE_NAME':'SEND_THANKS_',
          'ASK_BOTTOM_NAME':'SEND_THANKS_',       'SHOW_BOTTOM_':'SEND_THANKS_',       'SHOW_MORNING_RATIO_':'SEND_THANKS_',
          'ASK_MORNING_NAME':'SEND_THANKS_',       'SEND_THANKS_':'SEND_THANKS_',       'SEND_SORRY_':'SEND_THANKS_',
                 'SHOW_ACC_':'SEND_THANKS_'})

criticism=pd.Series({'INIT':'SEND_SORRY_',                 'ASK_NORTH_NAME':'SEND_SORRY_',    'SENDERROR_':'SEND_SORRY_',
           'SEND_TIME_ERROR_':'SEND_SORRY_',      'ASK_TIME':'SEND_SORRY_',    'ASK_ATTRIBUTE':'SEND_SORRY_',     
           'ASK_DAYS':'SEND_SORRY_',             'INTRO_':'SEND_SORRY_',              'SHOW_NORTH_':'SEND_SORRY_',        
           'SHOW_BASIC_':'SEND_SORRY_',            'SHOW_RATING_':'SEND_SORRY_',        'ASK_ATTRIBUTE_NAME':'SEND_SORRY_',
          'ASK_BOTTOM_NAME':'SEND_SORRY_',       'SHOW_BOTTOM_':'SEND_SORRY_',       'SHOW_MORNING_RATIO_':'SEND_SORRY_',
          'ASK_MORNING_NAME':'SEND_SORRY_',       'SEND_THANKS_':'SEND_SORRY_',       'SEND_SORRY_':'SEND_SORRY_',
                 'SHOW_ACC_':'SEND_SORRY_'})

criticism=pd.Series({'INIT':'SEND_SORRY_',                 'ASK_NORTH_NAME':'SEND_SORRY_',    'SENDERROR_':'SEND_SORRY_',
           'SEND_TIME_ERROR_':'SEND_SORRY_',      'ASK_TIME':'SEND_SORRY_',    'ASK_ATTRIBUTE':'SEND_SORRY_',     
           'ASK_DAYS':'SEND_SORRY_',             'INTRO_':'SEND_SORRY_',              'SHOW_NORTH_':'SEND_SORRY_',        
           'SHOW_BASIC_':'SEND_SORRY_',            'SHOW_RATING_':'SEND_SORRY_',        'ASK_ATTRIBUTE_NAME':'SEND_SORRY_',
          'ASK_BOTTOM_NAME':'SEND_SORRY_',       'SHOW_BOTTOM_':'SEND_SORRY_',       'SHOW_MORNING_RATIO_':'SEND_SORRY_',
          'ASK_MORNING_NAME':'SEND_SORRY_',       'SEND_THANKS_':'SEND_SORRY_',       'SEND_SORRY_':'SEND_SORRY_',
                 'SHOW_ACC_':'SEND_SORRY_'})
other=pd.Series({'INIT':'INIT',                 'ASK_NORTH_NAME':'INIT',    'SENDERROR_':'INIT',
           'SEND_TIME_ERROR_':'INIT',      'ASK_TIME':'INIT',    'ASK_ATTRIBUTE':'INIT',     
           'ASK_DAYS':'INIT',             'INTRO_':'INIT',              'SHOW_NORTH_':'INIT',        
           'SHOW_BASIC_':'INIT',            'SHOW_RATING_':'INIT',        'ASK_ATTRIBUTE_NAME':'INIT',
          'ASK_BOTTOM_NAME':'INIT',       'SHOW_BOTTOM_':'INIT',       'SHOW_MORNING_RATIO_':'INIT',
          'ASK_MORNING_NAME':'INIT',       'SEND_THANKS_':'INIT',       'SEND_SORRY_':'INIT',
                 'SHOW_ACC_':'INIT'})

policy_rules=pd.DataFrame({'ask_intro':ask_intro,'north_analysis':north_analysis,'name':name,'name_attribute':name_attribute,
                           'basic_attribute':basic_attribute,'non_latest_time':non_latest_time,'rating':rating,'period':period,
                           'north_buy_much_name':north_buy_much_name,'number':number,'north_buy_much_number_name':north_buy_much_number_name,
                           'double_bottom':double_bottom,'double_bottom_name':double_bottom_name,'morning_ratio_name':morning_ratio_name,
                           'morning_ratio':morning_ratio,'compliment':compliment,'other':other,'criticism':criticism})

