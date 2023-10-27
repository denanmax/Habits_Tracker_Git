import requests
from django.conf import settings


def tg_send_message(chat_id, text):
    """Процедура отправки сообщения в телеграм"""
    params = {'chat_id': chat_id, 'text': text}

    requests.get(f'https://api.telegram.org/bot{settings.API_TELEGRAM }/sendMessage',
                 params=params)
