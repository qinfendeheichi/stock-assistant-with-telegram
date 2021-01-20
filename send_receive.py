#!/usr/bin/env python
# coding: utf-8

import telegram
import base64
from io import BytesIO
import requests
import urllib.request, json

def get_my_info():
    """
    return the type of the message(user) id, message type, the content
    
    """  
    user_info_url='https://api.telegram.org/botmytoken/getUpdates'
    response = urllib.request.urlopen(user_info_url)
    data = json.loads(response.read())
    
    user_id=data['result'][len(data['result'])-1]['message']['from']['id']
    # print(data)
    # only text
    if 'text' in data['result'][len(data['result'])-1]['message'].keys():
        newest_text=data['result'][len(data['result'])-1]['message']['text']
        urllib.request.urlcleanup()
        return user_id,'text',newest_text
    #other message(can't reply correctly)
    else:
        return user_id,'document',None

def send_text(user_id,text):
    """
    send the designated text to the designated user, according to user_id
    
    """
    #transform the format of blank space and line break
    my_text=str(text).replace(' ','%20').replace('\n','%0a')

    send_url="https://api.telegram.org/botmytoken/sendMessage?chat_id="+str(user_id)+"&text="+my_text
    request = urllib.request.Request(url = send_url,method = 'POST')
    response = urllib.request.urlopen(send_url)
    urllib.request.urlcleanup()


def send_picture(user_id, file):
    """
    send a designated picture according to the location of a file
    """
    url = "https://api.telegram.org/botmytoken/sendPhoto";
    files = file
    data = {'chat_id' : user_id}
    r= requests.post(url, files=files, data=data)
    # print(r.status_code, r.reason, r.content)

