import logging
from datetime import datetime

import requests
from celery import shared_task
from django.conf import settings
from django.utils import timezone
from telebot import TeleBot
from habit.models import Habit
from users.services import tg_send_message


# @shared_task
# def habits_notification(**kwargs):
#     pk = kwargs.get('pk')
#     habit = Habit.objects.get(pk=pk)
#     tg_send_message(habit.user.chat_id, str(habit))


# @shared_task
# def habits_notification(*args, **kwargs):
#     logging.info("start")
#     pk = kwargs.get('pk')
#     if pk:
#         habit = Habit.objects.get(pk=pk)
#         tg_send_message(habit.user.chat_id, str(habit))
#         logging.info(f" ПК ВРЕМЯ! !!! {datetime.now()}")
#         logging.info(f"Сообщение - кому!!! {tg_send_message(habit.user.chat_id, str(habit))}")
#         return
#     habits = Habit.objects.all()
#     logging.info(habits)
#     for habit in habits:
#         logging.info(f"ВРЕМЯ !!! {habit.time}")
#         logging.info(f"Дата !!! {datetime.now()}")
#         if habit.time == datetime.now():
#             tg_send_message(habit.user.chat_id, str(habit))
#             logging.info(f"Сообщение - кому!!! {tg_send_message(habit.user.chat_id, str(habit))}")
#             return
#     logging.info("end")

@shared_task
def habits_notification(*args, **kwargs):
    logging.info("start")
    pk = kwargs.get('pk')
    if pk:
        habit = Habit.objects.get(pk=pk)
        tg_send_message(habit.user.chat_id, str(habit))
        logging.info(f"1 Сообщение - кому!!! {habit.user.chat_id} {str(habit)}")
        logging.info(f"1 ПК ВРЕМЯ! !!! {datetime.now()}")
        return

    current_time = datetime.now().time()
    habits = Habit.objects.filter(time__hour=current_time.hour, time__minute=current_time.minute)
    logging.info(habits)

    for habit in habits:
        logging.info(f"2 ВРЕМЯ !!! {habit.time}")
        logging.info(f"2 Дата !!! {datetime.now()}")

        tg_send_message(habit.user.chat_id, str(habit))
        logging.info(f"2 Сообщение - кому!!! {habit.user.chat_id}, {str(habit)})")

    logging.info("end")