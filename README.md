# zabbix_telegram_send_message
zabbix调用telegram_send_message

## 前提条件
tg bot api token 

在BotFather 处申请

## 安装依赖
听说python2也是可以使用的，未测试过，本人使用是python3.6
```
yum install python3-pip -y
pip3 install telegram
pip3  install python-telegram-bot
```

## zabbix script path
/usr/lib/zabbix/alertscripts/telegram_send_message.py

## test the py
三个参数
```
python3 /usr/lib/zabbix/alertscripts/telegram_send_message.py chat_id title context
```

## 寻找你的chat id
```
https://api.telegram.org/bot<YourBOTToken>/getUpdates
```

## zabbix web config
管理 -> 报警媒介类型 -> 创建媒介类型

脚本参数：
- {ALERT.SENDTO} 
- {ALERT.SUBJECT}
- {ALERT.MESSAGE}

配置 -> 动作 -> 创建动作

动作：
- 	 条件：触发器示警度 大于等于 警告

操作：
```
默认标题：  
服务器：{HOST.NAME}发生: {TRIGGER.NAME}故障！
 
消息内容： 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
告警主机:{HOST.NAME}
告警地址:{HOST.IP}
监控项目:{ITEM.NAME}
监控取值:{ITEM.LASTVALUE}
告警等级:{TRIGGER.SEVERITY}
当前状态:{TRIGGER.STATUS}
告警信息:{TRIGGER.NAME}
告警时间:{EVENT.DATE} {EVENT.TIME}
事件ID:{EVENT.ID}
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

操作：
发送消息给用户: Admin (Zabbix Administrator) 通过 zabbix2xxxtg_bot
立即地	默认
```
恢复操作：
```
默认标题：     
恢复服务器：{HOST.NAME}发生: {TRIGGER.NAME}故障恢复恢复恢复恢复恢复！

消息内容： 
================================================
告警主机:{HOST.NAME}
告警地址:{HOST.IP}
监控项目:{ITEM.NAME}
监控取值:{ITEM.LASTVALUE}
告警等级:{TRIGGER.SEVERITY}
当前状态:{TRIGGER.STATUS}
告警信息:{TRIGGER.NAME}
告警时间:{EVENT.DATE} {EVENT.TIME}
事件ID:{EVENT.ID}
================================================

操作：
发送消息给用户: Admin (Zabbix Administrator) 通过 zabbix2xxxtg_bot
立即地	默认
```

更新：
保持默认内容


## 用户账号配置
管理 -> 用户 -> 报警媒介
添加报警媒介类型为zabbix2xxxtg_bot，收件人处填写chat_id。即可
