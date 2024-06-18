# -*- coding:utf-8 -*-

import json
import time
from datetime import datetime
import requests
#from src.config import parse_args

def send_post_message(msg, url):
    headers = {'Content-Type': 'application/json'}

    #post_msg = {'user_message': str(msg)}
    post_msg = msg
    _post_data = json.dumps(post_msg, sort_keys=True, separators=(',', ':'))

    try:
        response = requests.post(url, data=_post_data, headers=headers)
        #print(response)
        result = response.json()

        print('Assistant:', result['return_message'].strip())
    except requests.exceptions.RequestException as e:
        print('[Error]:', e)

if __name__ == '__main__':
    #args = parse_args()
    lang = 'zh'
    
    #if args.lang == 'zh': 
    if lang == 'zh': 
        print('Assistant: 你好，今天有什麼事情想跟我聊聊嗎？')
    else: 
        print('Assistant: Hello, Is there anything you want to talk to me about today?')
    
    msg = {
	    "lang": <lang>,
	    "gender": <0 male or 1 female>,
	    "occupation": "<occupation>",
	    "self-assessed score": <phq-8 score>,
	    "user_id": <user_id>,
	    "user_name": "<user_name>",
	    "user_message": "",
	    "post_time": ""
	  }
    

    while True:
        input_str = input("User: ")
        if input_str == 'exit' or input_str == "結束對話":
            msg['user_message'] = "結束對話"
            break
        
        msg['user_message'] = input_str
        now = datetime.now()
        msg['post_time'] = now.strftime("%d/%m/%Y %H:%M:%S")
        
        send_post_message(msg, '<server url>')
    
    print('Assistant: 很高興你能與我分享煩惱，再見')
    msg['post_time'] = now.strftime("%d/%m/%Y %H:%M:%S")
    send_post_message(msg, '<server url>')
