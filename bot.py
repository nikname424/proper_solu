from telebot.async_telebot import AsyncTeleBot
from config import TOKEN
from markups1 import mainButtons, mainButtonsInline
import asyncio
import telebot

bot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start']) #для обработки сообщения
async def start(message: telebot.types.Message): #функция для обработки
    await bot.send_message(chat_id=message.from_user.id, text='hello', reply_markup=mainButtonsInline) #отправка сообщения

@bot.message_handler()
async def mess(message: telebot.types.Message):
    if message.text == 'Профиль':
        await bot.send_message(chat_id=message.from_user.id, text='Ваш профиль.', reply_markup=mainButtons) #отправка сообщения

@bot.callback_query_handler(func=lambda call: True)
async def getCall(call):
    if call.data == 'profile':
        await bot.send_message(chat_id=call.from_user.id, text='Ваш профиль.', reply_markup=mainButtons) #отправка сообщения

    if call.data == 'hello':
        await bot.send_message(chat_id=call.from_user.id, text='Привет', reply_markup=mainButtons) #отправка сообщения

    if call.data == 'help':
        await bot.send_message(chat_id=call.from_user.id, text='Помощь', reply_markup=mainButtons) #отправка сообщения

async def main():
    await asyncio.gather(bot.polling())

asyncio.run(main()) 
