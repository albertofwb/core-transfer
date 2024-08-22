import threading
import time
import requests
from private import TelegramConfig


class TgBot:
    def __init__(self, chat_id, bot_token):
        self.chat_id = chat_id
        self.bot_token = bot_token

    def notify(self, msg: str):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            'chat_id': self.chat_id,
            'text': msg,
            'parse_mode': 'HTML',
            'disable_web_page_preview': True
        }
        response = requests.post(url, data=payload)
        return response


def tg_notify(msg: str):
    if TelegramConfig.enable_notify:
        tg_bot = TgBot(TelegramConfig.chat_id, TelegramConfig.bot_token)
        tg_bot.notify(msg)


if __name__ == '__main__':
    tg_notify("Hello, World!")
