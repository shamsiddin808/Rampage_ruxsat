from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_check_ruxsat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="ha ruxsat✅", callback_data="ha_ruxsat"),
            InlineKeyboardButton(text="yoq task bor❌", callback_data="yoq_ruxsat")
        ]
    ]
)
