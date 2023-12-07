from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import logic
#from aiogram import ParseMode

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")

@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer("LOG help")

#messageLinkExample
#https://t.me/c/1401136600/18634
@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"message <a href = 'https://t.me/{msg.chat.username}/{msg.message_id}'> link </a> ",
                     parse_mode="HTML")
    #<a href="http://www.example.com/">inline URL</a>
    #await msg.answer(f"id сообщения: {msg}")
    #await msg.answer(f"id сообщения: {msg.message_id}")
    #await msg.answer(f"id чата: {msg.chat.id}")
    #await msg.answer(f"ссылка: https://t.me/c/1401136600/18634{msg.chat}")

    #await msg.answer(text = txt,
                     #parse_mode = "HTML")
#######################
#temporary Commands
@router.message(Command("addMaterials"))
async def start_handler(msg: Message):
    await msg.answer("LOG addMaterials")

@router.message(Command("addInstitution"))
async def start_handler(msg: Message):
    await msg.answer("LOG addInstitution")

@router.message(Command("register"))
async def start_handler(msg: Message):
    await msg.answer("LOG register")
    logic.registration.registration()
    logic.createPinnedMessage.createPinnedMessage(msg)
#######################
