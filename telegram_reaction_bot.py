import time
import sys
import pyfiglet
# Configuración de colores
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
B = "\033[1;34m"  # Blue
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(100.0 / 8000)

to(pyfiglet.figlet_format('SHORI'))
print(f'{R}by @Shorisound\n')
print(f'{R}https://t.me/Shorisound \n')
import requests
import random

def send_reaction(bot_token, chat_id, message_id):
    emojis = ["❤️‍🔥", "🤯", "🥰", '🔥', '😘', "🆒", "👍", "⚡", "👏", "😍", "🐳"]
    emoji = random.choice(emojis)
    url = f"https://api.telegram.org/bot{bot_token}/setMessageReaction"
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [
            {
                'type': 'emoji',
                'emoji': emoji
            }
        ],
        'is_big': False
    }
    response = requests.post(url, json=data)
    if response.json()['ok']:
        return f'Done √ {emoji}'
    else:
        return 'Error'

bot_tokens = ["","",""]
chat_id = "chat id"
link = input("Link==> ")
message_id = link.split('/')[4]

for bot_token in bot_tokens:
    print(send_reaction(bot_token, chat_id, message_id))