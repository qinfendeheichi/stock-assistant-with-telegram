#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import datetime
import warnings
warnings.filterwarnings("ignore")
import translators as ts

def text_rating_(state:[str], recorder:[list]):-> 'str:the content of the text to be returned to the user'
    """
    get the text of info released within desigabout special ratings of securities from 
    some top security companies in China.
    """
    try:
        df=pd.read_excel('rating_july.xlsx')
        text="Results:\n\n"
        if len(recorder)==1:
            result=df[df['date']==recorder[0]]
        else:   
            result=df[(df['date']>=recorder[0]) & (df['date']<=recorder[1])]
        for i in range(len(result)):
            data=result.iloc[i]
            text=text+"name:"+data['name']+            "\n"+"code:"+str(data['code'])+"\n"+            "date:"+str(data['date'].date())+"\n"+            "rating_agency:"+data['rating_agency']+            "\n"+"evaluation:"+data['rating']+"\n\n"
        if "强烈看多" in text:
            text=text.replace("强烈看多","strongly bullish")
        try:
            text=ts.bing(text, if_use_cn_host=True)
        except:
            pass
        return text
    except:
        return "something wrong has happend!"


