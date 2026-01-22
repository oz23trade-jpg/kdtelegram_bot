from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from texts import load_texts, t
from keyboards.inline import language_kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    load_texts("en")
    await message.answer(t("welcome"), reply_markup=language_kb())
