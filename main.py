from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN
from handlers import start, order

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start.register_handlers(dp)
order.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)