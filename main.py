from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.filters import Command

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

# dp.run_polling()
async def main():
    await dp.start_polling()

@dp.message(Command[commands = ["start"]])

run(main()) # запускает цикл событий ()