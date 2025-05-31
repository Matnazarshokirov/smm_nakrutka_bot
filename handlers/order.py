from aiogram import types, Dispatcher
from services.smm_api import create_order

async def order_service(message: types.Message):
    await message.reply("ðŸ”§ Buyurtma yuborilmoqda...")
    result = create_order(service_id=1, link="https://t.me/example", quantity=100)
    await message.reply(f"âœ… Buyurtma holati: {result}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(order_service, commands=["order"])
