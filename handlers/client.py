from aiogram import Bot, types
from create_bot import dp, bot
from aiogram.dispatcher import Dispatcher
from keyboards import kb_client
# from aiogram.types import ReplyKeyboardRemove, \
#     ReplyKeyboardMarkup, KeyboardButton, \
#     InlineKeyboardMarkup, InlineKeyboardButton
from database import sqlite
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InputFile
from datetime import datetime

# class FSMClient(StatesGroup):
#     term = State()
#     subjects = State()

# @dp.message_handler(commands=['start'])
# async def command_start(message : types.Message):
#     await message.answer('Привет, выбери команду', reply_markup=kb_client)

@dp.message_handler(commands=['timetable'])
async def shedule_lessons(message : types.Message):
    res = await sqlite.get_timetable()
    today = datetime.today()
    if(today.weekday() > 4):
        res = await sqlite.get_timetable()
        await bot.send_photo(chat_id=message.chat.id, photo=res)
    else:
        await message.answer(res, parse_mode='Markdown')
    # msg = await message.reply('1', reply_markup=types.ReplyKeyboardRemove())
    # await msg.delete()

# @dp.message_handler(commands=['exams'], state=None)
# async def prepare_exams(message : types.Message):
#     await FSMClient.term.set()
#     await message.reply('Семестр:', reply_markup=semestr_kb.kb_semestr)



# @dp.message_handler(content_types=['text'] ,state=FSMClient.term)
# async def get_subjects(message: types.Message, state:FSMContext):
#     async with state.proxy() as data:
#         data['term'] = message.text
#     await FSMClient.next()
#     res = sqlite.subject(data['term'])
#     msg = await message.reply('1', reply_markup=types.ReplyKeyboardRemove())
#     await msg.delete()
#     await subjects_kb.get_subj(data['term'])
#     await message.answer('Предмет:', reply_markup=subjects_kb.kb_subjects)
    


# @dp.message_handler(content_types=['text'], state=FSMClient.subjects)
# async def get_term(message : types.Message, state:FSMContext):
#     async with state.proxy() as data:
#         data['subjects'] = message.text
#     res = sqlite.sql_get_data(data['subjects'], data['term'])
#     await message.reply_document(open(res, 'rb'))
#     msg = await message.answer('end', reply_markup=types.ReplyKeyboardRemove())
#     await msg.delete()
#     await state.finish()


def register_handlers_client(dp : Dispatcher):
    # dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(shedule_lessons,commands=['расписание'])
    # dp.register_message_handler(prepare_exams, commands=['экзамен'])
    # dp.register_message_handler(get_subjects, commands=['Предметы'])