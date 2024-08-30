from telebot.async_telebot import AsyncTeleBot
from config import TOKEN
from markups import mainButton, mainButtonInline
import asyncio
import telebot

bot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start']) #для обработки сообщения
async def start(message: telebot.types.Message): #функция для обработки
    await bot.send_message(chat_id=message.from_user.id, text='hello', reply_markup=mainButtonInline) #отправка сообщения

@bot.message_handler(commands=['photo']) #для отправки фотографии
async def photo(message: telebot.types.Message): #функция для обработки
    with open('main_icon.png', 'rb') as file:
        await bot.send_photo(chat_id=message.from_user.id, photo=file)

async def main():
    await asyncio.gather(bot.polling())

asyncio.run(main())