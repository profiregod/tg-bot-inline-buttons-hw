from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import like_callback, dislike_callback
from loader import dp


rating = {}


@dp.callback_query_handler(like_callback.filter())
async def rating_item(call: CallbackQuery, callback_data: dict):
    item_id = callback_data.get("item_id")
    rating[item_id] = rating[item_id] + 1 if hasattr(rating, item_id) else 1
    await call.answer(f"Вы поставили лайк товару #{item_id}!\n", show_alert=False)


@dp.callback_query_handler(dislike_callback.filter())
async def rating_item(call: CallbackQuery, callback_data: dict):
    item_id = callback_data.get("item_id")
    rating[item_id] = rating[item_id] - 1 if hasattr(rating, item_id) else -1
    await call.answer(f"Вы поставили дизлайк товару #{item_id}!\n", show_alert=False)
