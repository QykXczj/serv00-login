import requests
import os

# 从环境变量中获取 Telegram Bot Token 和 Chat ID
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
VX_BOT_KEY = os.getenv('VX_BOT_KEY')

def send_message(message):
    send_telegram_message(message)
    send_VX_Bot_message(message)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"发送消息到Telegram失败: {response.text}")
    except Exception as e:
        print(f"发送消息到Telegram时出错: {e}")

def send_VX_Bot_message(message):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={VX_BOT_KEY}"
    payload = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"发送消息到VX_BOT失败: {response.text}")
    except Exception as e:
        print(f"发送消息到VX_Bot时出错: {e}")

send_message("hax该续了https://hax.co.id/vps-renew/")
