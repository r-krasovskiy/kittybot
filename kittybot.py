"""Библиотека для работы с ботами Телеграм."""
from telegram import Bot

bot = Bot(token='6979293587:AAGaLUmvnnK6bdlrlGf1NGFglq9RFj9Hj80')

chat_id = 193802815
text = 'Вам телеграмма!'
bot.send_message(chat_id, text)
