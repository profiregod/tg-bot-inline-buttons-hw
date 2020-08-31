from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купить товар", callback_data="buy:mandarin:1"),
    ],
    [
        InlineKeyboardButton(text="👍", callback_data="like:mandarin:1"),
        InlineKeyboardButton(text="👎", callback_data="dislike:mandarin:1"),
    ],
    [
        InlineKeyboardButton(text="Отправить другу", switch_inline_query="1"),
    ],
])
