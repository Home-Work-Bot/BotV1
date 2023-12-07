from .. import data

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
def createOneSubjectMessage(prev, name:str, data):
    #msg.answer()
    pass

def createPinnedMessage(msg: Message):
    subjects = data.getData.getData(msg.message_id)
    links = []
    for s in subjects:
        createOneSubjectMessage(None, s, None)

