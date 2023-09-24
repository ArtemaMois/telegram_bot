from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from database import sqlite
sqlite.db_start()


# kb_subjects = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# async def get_subj(sem):
#     res = sqlite.subject(sem)
#     for i in range(0, len(res)):
#         button = KeyboardButton(res[i])
#         kb_subjects.add(button)



