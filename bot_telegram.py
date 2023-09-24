from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from database import sqlite





async def on_startup(_):
    print('Бот онлайн')
    sqlite.db_start()

client.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


