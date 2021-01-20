#!/usr/bin/env python
# coding: utf-8

from jqdatasdk import *
auth('phone number','password')

import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
import datetime as dt
import warnings
import datetime
warnings.filterwarnings("ignore")

def show_acc_(state,recorder):
    """
    display the ratio of shares of a stock hold by north-oriented money
    for the consecutive several days
    """
    try:
        if isinstance(recorder[0],str) and len(recorder[0])==6:
            day_number=recorder[1]
            stock=recorder[0]
        else:
            day_number=recorder[0]
            stock=recorder[1]

        if stock[0]=='0' or stock[0]=='3':
            stock=stock+'.XSHE'
        else:
            stock=stock+'.XSHG'

        table = finance.STK_HK_HOLD_INFO
        all_days=get_trade_days(count=day_number)
        def get_north_days(trade_days):
            north_days=[]
            for i in all_days:
                q = query(table.day, table.name, table.code, table.share_ratio).filter(table.link_id.in_(['310002','310001']),table.day.in_([i]))
                df = finance.run_query(q)
                if len(df)!=0:
                    north_days.append(i)
            return north_days
        share=[]
        north_days=get_north_days(all_days)
        for date in north_days:
            q = query(table.day, table.name, table.code, table.share_ratio).filter(table.link_id.in_(['310002','310001']),table.day.in_([date]))
            df12 = finance.run_query(q)
            df12=df12.sort_values(by='share_ratio',ascending=False)[:][['code','name','share_ratio']]
            share.append(df12[df12['code']==stock]['share_ratio'].values[0])
        plt.figure(figsize=(10,7))
        plt.bar(north_days[-day_number:],(np.array(share))[-day_number:],label='hold ratio of the latest '+str(day_number)+' days')
        plt.legend()
        plt.title(stock)
        plt.savefig('picture\\my'+'.png')
        plt.clf()
        return 'picture\\my.png'
    except:
        return 'picture\\error.png'

