from aiogram.utils.callback_data import CallbackData


buy_callback = CallbackData("buy", "item", "item_id")

like_callback = CallbackData("like", "item", "item_id")

dislike_callback = CallbackData("dislike", "item", "item_id")
