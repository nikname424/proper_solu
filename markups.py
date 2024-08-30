from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

mainButton = ReplyKeyboardMarkup(resize_keyboard=True)

profilButton = KeyboardButton("Профиль")
helpButton = KeyboardButton("Помощь")
helloButton = KeyboardButton("Привет")

mainButton.add(profilButton, helloButton, helpButton)

################3
profileButtonInline = InlineKeyboardButton('Профиль', callback_data='profile')
helpButtonInline = InlineKeyboardButton('Помощь', callback_data='help')
helloButtonInline = InlineKeyboardButton('Привет', callback_data='hello')

mainButtonInline = InlineKeyboardMarkup()
mainButtonInline.add(profileButtonInline, helloButtonInline, helpButtonInline)
