from config import dp, Bot, Admins
from aiogram.utils import executor
import logging
import asyncio
from handlers import client
# ===================================================================================
async def on_startup(_):
    await Bot.send_message(chat_id=Admins[0],text="Бот запущен!")
# ===================================================================================
client.handler_client(dp)
# ===================================================================================
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
# ===================================================================================

