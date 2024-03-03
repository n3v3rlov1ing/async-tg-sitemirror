from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

import config as cfg

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Привет, напиши /link для получения ссылки на зеркало')
    
@router.message(Command('link'))
async def cmd_link(message: Message):
    buttons = []
    for i, _ in cfg.urls.items():
        buttons.append([InlineKeyboardButton(text=i, url=_)])
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer('Нажмите на кнопку, чтобы прейти', reply_markup=kb)