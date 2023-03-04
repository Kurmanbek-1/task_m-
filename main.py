from config import dp
from aiogram.utils import executor
import logging
import asyncio
from handlers import client
# ===================================================================================
client.handler_client(dp)
# ===================================================================================
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
# ===================================================================================

