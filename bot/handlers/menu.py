from aiogram import Router, F
from aiogram.types import CallbackQuery

from texts import t

router = Router()

@router.callback_query(F.data.startswith("menu_"))
async def menu(cb: CallbackQuery):
    await cb.message.edit_text(t("main_menu"))
    await cb.answer()
