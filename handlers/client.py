from config import Bot
from aiogram import types, Dispatcher
from addition import get_message, film_emogi, horror_stories
from keyboards.client_kb import start_markup
# ===================================================================================
async def start_handler(message: types.Message):
    await Bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}",
                           reply_markup=start_markup)
    await message.answer('/info - просмотр команд'
                         '/infobot - документация о боте')
# -----------------------------------------------------------------------------------
async def info_handler(message: types.Message):
    await message.answer('В этом боте присутствует: \n'
                         '/find - любой запрос?\n'
                         '/film - поиск фильмов по эмоджи\n'
                         '/hs - напишет историю, только нужно ввести начало \n'
                         '====================================\n'
                         'Писать так: /find ... \n'
                         '/hs писать так - "/hs история со школы. Полностью на русском. '
                         'Состоящем из 4 предложений"\n')
# -----------------------------------------------------------------------------------
async def infobot(message: types.Message):
    await message.answer('Этот бот может найти любую информацию через команду "/find". '
                         'Находить фильмы по эмоджи через '
                         'команду "/film", допустим "/film 🪄⚡️🧙🏼"')
# -----------------------------------------------------------------------------------
async def find(message: types.Message):
    await message.answer(get_message(message))
# -----------------------------------------------------------------------------------
async def film(message: types.Message):
    await message.answer(film_emogi(message))
# -----------------------------------------------------------------------------------
async def stories(message: types.Message):
    await message.answer(horror_stories(message))
# ===================================================================================
def handler_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(find, commands=['find'])
    dp.register_message_handler(film, commands=['film'])
    dp.register_message_handler(stories, commands=['hs'])