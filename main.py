from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.filters import Command
from aiogram.types import Message
from requests import get
from random import choice
from aiogram import F
# dp.run_polling()


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    @dp.message(F.text.contains("start") )
    async def start_handler(message: Message):
        await message.answer(f"Привет {F.from_user.username}")
    await dp.start_polling(bot)

    @dp.message(F.from_user.username == "yarchhee")
    async def get_me_stat(message: Message):
        await message.answer("Вот тебе стата")

print(f"[LOG] Бот запущен")
run(main()) # запускает цикл событий