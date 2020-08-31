from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.item_keyboard import choice
from loader import dp


@dp.message_handler(Command("item"))
async def show_item(message: Message):
    await message.answer_photo(
        photo="https://lh3.googleusercontent.com/proxy/W--coAUEuOnWu4BYRGX6-DIf88XT6RBpYPdK1IxkcibXQuKJq0AAwqw3QukavNkJzarlIe-8ASy6DAE84eATeKorVnVl4KHAqA6PmqrHfZY",
        caption="Мандарин",
        reply_markup=choice
    )


@dp.callback_query_handler(buy_callback.filter(item_id="1"))
async def buying_mandarin(call: CallbackQuery, callback_data: dict):
    item_id = callback_data.get("item_id")
    await call.message.edit_caption(
        caption=f"Покупай товар номер {item_id}",
        reply_markup=None
    )
