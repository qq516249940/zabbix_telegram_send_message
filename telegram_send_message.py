#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-*

#Author: chunk
#Date:   2019-12-26 18:59:26
#Description:Zabbix use telegram bot to send message to group**

import telegram
import sys

contact = sys.argv[1]
subject = sys.argv[2]
content = sys.argv[3]

bot = telegram.Bot(token='xxxx:xxxxxxxxxxxxxxxxxx')
chat_id = contact

bot.send_message(chat_id=chat_id, text=subject+'\n'+content)
