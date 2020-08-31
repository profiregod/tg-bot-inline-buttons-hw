from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купить товар", callback_data="buy:1"),
    ],
    [
        InlineKeyboardButton(text="👍", callback_data="like:1"),
        InlineKeyboardButton(text="👎", callback_data="dislike:1"),
    ],
    [
        InlineKeyboardButton(text="Отправить другу", switch_inline_query="1"),
    ],
])
