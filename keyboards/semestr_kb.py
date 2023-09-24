from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from database import sqlite
sqlite.db_start()

semestr = sqlite.get_semestr();

# kb_semestr = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# for i in range(0, len(semestr)):
#     button = KeyboardButton(semestr[i])
#     kb_semestr.add(button)


