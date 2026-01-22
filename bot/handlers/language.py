from aiogram import Router, F
from aiogram.types import CallbackQuery

from texts import load_texts, t
from keyboards.inline import main_menu_kb

router = Router()

@router.callback_query(F.data.startswith("lang_"))
async def set_language(cb: CallbackQuery):
    lang = cb.data.split("_")[1]
    load_texts(lang)
    await cb.message.edit_text(t("language_set"), reply_markup=main_menu_kb())
    await cb.answer()
