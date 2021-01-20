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

def show_morning_ratio_(state,recorder):
    """
    show the ratio of transacitons created in the first 15 minutes of the trading time
    within the latest several days
    Only the last trade day's result can be retrieved
    
    """
    try:
        stock=recorder[0]
        if stock[0]=='0' or stock[0]=='3':
            stock=stock+'.XSHE'
        else:
            stock=stock+'.XSHG'
        security=stock

        m_number=10*240
        min_price=get_bars(security, m_number, unit='1m',fields=('volume','date', 'open', 'high', 'low', 'close'),include_now=False,end_dt=datetime.date.today(),fq_ref_date=None,df=False)
        df_min_price=pd.DataFrame(min_price)

        df_min_price=df_min_price[(df_min_price['date']>datetime.date.today()-datetime.timedelta(days=7)) & (df_min_price['date']<datetime.date.today()+datetime.timedelta(days=1))]
        df_min_price=pd.DataFrame([j.tolist() for i,j in enumerate(df_min_price.values) if (i%240<=14)])

        df_min_price.iloc[:,1]=[np.datetime64(i,'D').tolist() for i in list(df_min_price.iloc[:,1].values)]
        last=df_min_price.groupby([1],as_index=True)[0].sum()
        plt.figure(figsize=(10,7))
        plt.bar(x=list(last.index),height=list(last/10000000),label='morning_15_ratio')
        plt.legend()

        plt.savefig('picture\\my'+'.png')
        plt.clf()
        return 'picture\\my.png'
    except:
        return 'picture\\error.png'

# an example
# show_morning_ratio_('ini',['000001'])

