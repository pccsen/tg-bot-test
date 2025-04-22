from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirm_data_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm_data"),
            InlineKeyboardButton(text="🔁 Изменить", callback_data="edit_data")
        ]
    ]
)
thank_you_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Спасибо!", callback_data="thank_you")
        ]
    ]
)