from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# ===================================================================================
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    row_width=3
)
# ===================================================================================
start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')
# ===================================================================================
start_markup.add(start_button, info_button)
# ===================================================================================

