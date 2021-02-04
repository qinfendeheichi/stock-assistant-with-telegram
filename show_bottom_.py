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
import math

def find_lowest(x,y,standard_data):
    """
    find the lowest price between week x and week y, 
    all attributes are meassureed by the unit 'week'
    
    x  the date of the left boundary
    y  the date of the right boundary
    standard_data    stock info dataframe
    """
    lowest=9999
    result_date=None
    for i in standard_data.values:
        if i[0].__ge__(x) and i[0].__le__(y):
            if i[3]<lowest:
                lowest=i[3]
                result_date=i[0]
    #day x and y are not included
    if result_date.__eq__(x) or result_date.__eq__(y):
        return None
    return result_date
# find_lowest(x,y,standard_data)

def E1(C,E,standard_data):
    """
    whether the volume of E is more the average volume
    between point C and point E
    """
    #volume of E
    volume_E=standard_data.values[standard_data.values[:,0].__eq__(E)][0][5]
    #the average volume between C and E
    volume_CE=standard_data.values[standard_data.values[:,0].__gt__(C) & standard_data.values[:,0].__lt__(E)][:,-1].mean()
    
    if volume_E>volume_CE*1.2:
        return True
    else:
        return False
# E1(C,E,standard_data)

def E2(C,E,standard_data):
    """
    The highest price of E should be more than the that of C
    and, it shouldn't be more than 1.05*C
    """
    #the highest price of point E
    price_E=standard_data.values[standard_data.values[:,0]==E][0][2]
    #the highest price of point C
    price_C=standard_data.values[standard_data.values[:,0]==C][0][2]
    
    if price_E>price_C and price_E/price_C<1.05:
        return True
    else:
        return False
# E2(C,E,standard_data)

def E3(C,E,standard_data):
    """
    the open price of E isn' t the highest price of E
    """
    #the highest price of E
    price_E=standard_data.values[standard_data.values[:,0]==E][0][2]
    #the open price of E
    price_E_open=standard_data.values[standard_data.values[:,0]==E][0][1]
#     print(price_E,price_E_open)
    
    if(price_E_open!=price_E):
        return True
    else:
        return False
# E3(C,E,standard_data)

def judge_E(C,E,standard_data):
    """
    whether it satisfies the all three requirements of E
    """
    if E1(C,E,standard_data)and E2(C,E,standard_data)and E3(C,E,standard_data):
        return True
    else:
        return False
# judge_E(C,E,standard_data)

def C1(C,D,E,A,B,standard_data):
    """
    the highest price of C should be more than the 
    highest price between C and E
    """
    
    #the highest price of C
    price_C=standard_data.values[standard_data.values[:,0]==C][0][2]

    # the highest price between C and E
    price_CD=standard_data.values[standard_data.values[:,0].__gt__(C) & standard_data.values[:,0].__le__(D)][:,2]

    if price_C>price_CD.max():
        return True
    else:
        return False
# C1(C,D,E,A,B,standard_data)

def C2(C,D,E,A,B,standard_data):
    """
    the highest price of E should be more than 
    the highest price between C and E  
    """
 
    #the highest price of E
    price_E=standard_data.values[standard_data.values[:,0]==E][0][2]
    
    #the highest price bewtween C and E
    price_DE=standard_data.values[standard_data.values[:,0].__ge__(D) & standard_data.values[:,0].__lt__(E)][:,2]
    
    if price_E>price_DE.max():
        return True
    else:
        return False

def C3(C,D,E,A,B,standard_data):
    """
    the depth of D:
    the depth from D to A should be between 15%-20%
    """
    #the lowest price of D
    price_D=standard_data.values[standard_data.values[:,0]==D][0][3]
    #the highest price of A
    price_A=standard_data.values[standard_data.values[:,0]==A][0][2]

    if price_D/price_A<0.85 and price_D/price_A>0.5:
        return True
    else:
        return False
# C3(C,D,E,A,B,standard_data) 

def C4(C,D,E,A,B,standard_data):
    """
    the lowest price between C and E should be lower than 
    the lowest price bewtween AC
    """
    #the lowest price of D
    price_D=standard_data.values[standard_data.values[:,0]==D][0][3]
    #the lowest price of B
    price_B=standard_data.values[standard_data.values[:,0]==B][0][3]
    if(price_D<price_B):
        return True
    else:
        return False

def C5(C,D,E,A,B,standard_data):
    """
    the highest price of B - the lowest price of B
    should be more than the length between A and B
    """
    
    #the highest price of C
    price_C=standard_data.values[standard_data.values[:,0]==C][0][2]
    #the highest price of A
    price_A=standard_data.values[standard_data.values[:,0]==A][0][2]
    #the lowest price of B
    price_B=standard_data.values[standard_data.values[:,0]==B][0][3]
    if (price_C-price_B)>1/4*(price_A-price_B) and price_C-price_B>0 and (price_A-price_B)>0:
        
        return True
    else:
        return False

def judge_C(C,D,E,A,B,standard_data):
    """
    whether it satisfies the all three requirements of C
    """
    if C1(C,D,E,A,B,standard_data) and C2(C,D,E,A,B,standard_data) and C3(C,D,E,A,B,standard_data) and C4(C,D,E,A,B,standard_data) and C5(C,D,E,A,B,standard_data):
        return True
    else:
        return False
# judge_C(C,D,E,A,B,standard_data)

def A1(A,B,C,D,standard_data):
    """
    the lowest price bewtween A and the price of 60 weeks ago should be 
    more than 130% of the price of A
    """
    
    #data before period A
    temp=standard_data.values[standard_data.values[:,0].__lt__(A)]
    #the lowest price before period A
    price_A_min=temp[:,3].min()
    # the highest price before period A
    price_A_max=temp[:,3].max()
    
    if price_A_max/price_A_min>1.3:
        return True
    else:
        return False

def A2(A,B,C,D,standard_data):
    """the highest price of A should be more than 
    the highest price bewteen A and B
    """
    
    #the highest price of A
    price_A=standard_data.values[standard_data.values[:,0]==A][0][2]
    
    #the highest price between A and B
    price_AB=standard_data.values[standard_data.values[:,0].__gt__(A) & standard_data.values[:,0].__le__(B)][:,2]
    
    if price_A>price_AB.max():
        return True
    else:
        return False

def A3(A,B,C,D,standard_data):
    """
    the highest price of C should be more than 
    the highest price bewtween B and C
    """
    
    #the highest price of C
    price_C=standard_data.values[standard_data.values[:,0]==C][0][2]
    
    #the highest price between B and C
    price_BC=standard_data.values[standard_data.values[:,0].__ge__(B) & standard_data.values[:,0].__lt__(C)][:,2]

    if price_C>price_BC.max():
        return True
    else:
        return False

def A4(A,B,C,D,standard_data):
    """
    the highest price of C should be more than 
     the highest price between B and C
    """
    
    #the highest price of A
    price_A=standard_data.values[standard_data.values[:,0]==A][0][2]  
    #the highest price of C
    price_C=standard_data.values[standard_data.values[:,0]==C][0][2]
    
    if(price_A>price_C):
        return True
    else:
        return False
    
    # A4(A,B,C,D,standard_data)    

def judge_A(A,B,C,D,standard_data):
    """whether it satisfies the all three requirements of A"""
    #     print(A3(A,B,C,D,standard_data))
    if A1(A,B,C,D,standard_data) and A2(A,B,C,D,standard_data) and A3(A,B,C,D,standard_data) and A4(A,B,C,D,standard_data):
        return True
    else:
        return False
    
    # judge_A(A,B,C,D,standard_data)

def recognize(security,date,m,n):
    """
    if it is a proper date to be the point E for forming the double bottom state
    """
    
    #the picture should be between 15-18 weeks
    
    x=get_bars(security, 300, unit='1d',fields=['date','open','high','low','close','volume'],include_now=False,end_dt=datetime.date.today()+datetime.timedelta(days=1),df=True)
    p=np.array(x['date'])
    end_dt=p[list(p).index(date)+1]
    
    history_data= get_bars(security, 60, unit='1w',fields=['date','open','high','low','close','volume'],include_now=False,end_dt=end_dt)
    #transform the data into dataframe
    standard_data=pd.DataFrame(history_data)
    list_data=list(standard_data.values)
    
    for A in list(standard_data.values[-n-1:-m-1][:,0]):
        left_limit=list(standard_data.values[:,0]).index(A)+2
        for C in standard_data.values[:,0][left_limit:-2]:
            #get point B
            B=find_lowest(A,C,standard_data)
            if B==None:
                continue
            #get point D
            D=find_lowest(C,date,standard_data)
            if D==None:
                continue

            if judge_E(C,date,standard_data) and judge_C(C,D,date,A,B,standard_data) and judge_A(A,B,C,D,standard_data):
                return A,B,C,D,date
    return None

def test_a_stock(security):
    """test a stock
    """
    date=datetime.date.today()+datetime.timedelta(days=1)
    history_data= get_bars(security, 40, unit='1w',fields=['date','open','high','low','close','volume'],include_now=False,end_dt=date)
    #     print(history_data)
    #     print('ok')
        my_date=[]
    #     history_data.iloc[0]['date']
    #     for i in history_data:
    #         my_date.append(i[0])
    my_date=list(history_data['date'])
    # print(my_date[0])
    shape=[]
    for i in my_date:
    # it should be between 12-25 weeks
        x=recognize(security,i,12,25)
        if x!=None:
            shape.append(x)
    return shape

def paint(security):
    shape=test_a_stock(security)
    end_dt=datetime.date.today()
    #get all trade days
    all_days=get_all_trade_days()

    history_data= get_bars(security, 60, unit='1w',fields=['date','open','high','low','close','volume'],include_now=False,end_dt=end_dt)
    standard_data=pd.DataFrame(history_data)

    #picture time: 100days before A-100days after
    m=int(math.sqrt(len(shape)))+1
    plt.figure(figsize=(10,7*len(shape)), dpi=100)
    for i in list(range(len(shape))):

        plt.figure(1)
        plt.subplot(len(shape),1 , i+1)
        pic_date=[]
        left_index=list(all_days).index(shape[i][0])-100
        right_index=list(all_days).index(shape[i][4])+100
        pic_date=all_days[left_index:right_index]
        
        price_A=standard_data.values[standard_data.values[:,0]==shape[i][0]][0][2]
        price_B=standard_data.values[standard_data.values[:,0]==shape[i][1]][0][3]
        price_C=standard_data.values[standard_data.values[:,0]==shape[i][2]][0][2]
        price_D=standard_data.values[standard_data.values[:,0]==shape[i][3]][0][3]
        price_E=standard_data.values[standard_data.values[:,0]==shape[i][4]][0][2]
        
        close_price_daily=get_price(security, start_date=pic_date[0], end_date=pic_date[-1], frequency='daily', fields=None, skip_paused=False, fq='pre', count=None, panel=True, fill_paused=True)['close']
        volume_daily=get_price(security, start_date=pic_date[0], end_date=pic_date[-1], frequency='daily', fields=None, skip_paused=False, fq='pre', count=None, panel=True, fill_paused=True)['volume']
        # print(close_price_daily)
        plt.plot(close_price_daily)
        plt.plot(shape[i],[price_A,price_B,price_C,price_D,price_E],'-',color='black',markeredgewidth=0.5)
       
    
        #ajust the para of volume
        a=(volume_daily/price_A*30).values[-1]
        plt.bar(volume_daily.index,volume_daily/a,color='red')
        plt.title("close_price_daily:%s"% i)
        plt.ylabel('daily_close_price, volume/%s' %a)
        plt.ylim(0)
        #annotate the point ABCDE
        txt = ['A','B','C','D','E']
        for j in list(range(5)):
            plt.annotate(txt[j],xy=(shape[i][j],[price_A,price_B,price_C,price_D,price_E][j]),color='red') 

def show_bottom_(state, record):
    try:
        stock=record[0]
        if stock[0]=='0' or stock[0]=='3':
            stock=stock+'.XSHE'
        else:
            stock=stock+'.XSHG'
        paint(stock)
        plt.savefig('picture\\my'+'.png')
        plt.clf()
        return 'picture\\my.png'
    except:
        return 'picture\\error.jpg'

# an example
# show_bottom_('init',['002537'])

