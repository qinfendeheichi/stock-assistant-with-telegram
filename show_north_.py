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

def show_north_(state:[str],recorder:"list,the length should be 1")->"the location of the returning picture":
    """
    It shows the north-oriented money flowing from foreign countries or HongKong 
    to China's stock market in the latest 15 days. 
    
    """
    try:
        if len(recorder)==1:
            stock=recorder[0]
            if stock[0]=='0' or stock[0]=='3':
                stock=stock+'.XSHE'
            else:
                stock=stock+'.XSHG'
            day_number=15
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

            data=get_price(stock,end_date=datetime.date.today(),count=day_number)['close']

            #standardization of the price
            test_price=np.array(data[north_days].values)
            mean_price=np.mean(test_price)
            var_price=np.var(test_price)
            std_price=(test_price-np.mean(test_price))/var_price
            
            #standardization of hold ratio
            test_share=np.array(share)
            mean_share=np.mean(test_share)
            var_share=np.var(test_share)
            std_share=(test_share-np.mean(test_share))/var_share  

            para=test_price[0]/test_share[0]/2
            plt.clf()
            plt.figure(figsize=(10,7))
            plt.plot(north_days,np.array(share)*para,label='scaled ratio')
            plt.bar(north_days[-15:],(np.array(share)*para)[-15:],label='the latest 15 days')
            plt.legend()
            plt.title(stock)
            plt.savefig('picture\\my'+'.png')
            return 'picture\\my.png'
    except:
        return 'picture\\error.png'
 

# an example
# show_north_('show_north',['000100'])


