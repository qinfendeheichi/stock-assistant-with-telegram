#!/usr/bin/env python
# coding: utf-8

from jqdatasdk import *
auth('telephone number','password')

import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
import datetime as dt
import warnings
import datetime
warnings.filterwarnings("ignore")

def show_basic_(state,recorder):
    
    """
    show the basic attribute of a stock 
    unfortunately, the module now doesn't support query with the attribute"volume"
    """
    try:
        if isinstance(recorder[0],str):
            stock=recorder[0]
            attribute=recorder[1]
        else:
            stock=recorder[1]
            attribute=recorder[0]

        if stock[0]=='0' or stock[0]=='3':
            stock=stock+'.XSHE'
        else:
            stock=stock+'.XSHG'

        data=get_bars(stock,count=30,unit='1m',include_now=True)
        time=[i.time() for i in data['date']]
        plt.xticks=time
        if attribute=='price':
            attribute='close'
        plt.figure(figsize=(10,7))
        plt.plot(data[attribute])
        plt.ylabel(attribute)
        plt.xlabel('time(the latest 30 minutes)')
        plt.title('the last 30 minutes')
        plt.savefig('picture\\my'+'.png')
        plt.clf()
        return 'picture\\my.png'
    except:
        return 'picture\\error.png'

# an example
# show_basic_('SHOW_BASIC_',('000100','price'))

