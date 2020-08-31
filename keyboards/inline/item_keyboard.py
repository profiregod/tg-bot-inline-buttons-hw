from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback


choice = InlineKeyboardMarkup(row_width=2)

# Добавляем кнопки
buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data="buy:pear:1")
# buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Купить яяблоки", callback_data="buy:apple:5")
choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Отменить", callback_data="cancel")
choice.insert(cancel_button)

# Клавиатуры конкретных товаров
pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купить грушу по ссылке", url="http://ya.ru")
    ]
])

apple_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купить яблоки по ссылке", url="http://yandex.ru")
    ]
])

