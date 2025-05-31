from aiogram import types, Dispatcher
from templates import START_TEXT, PAYMENT_INFO

async def cmd_start(message: types.Message):
    await message.answer(START_TEXT)
    await message.answer(PAYMENT_INFO)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
