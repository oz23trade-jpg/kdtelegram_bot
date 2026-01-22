from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def language_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇫🇮 Suomi", callback_data="lang_fi")]
    ])

def main_menu_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 Learning", callback_data="menu_learning")],
        [InlineKeyboardButton(text="💰 Earn", callback_data="menu_earn")],
        [InlineKeyboardButton(text="❤️ Support ☕", callback_data="menu_support")]
    ])
