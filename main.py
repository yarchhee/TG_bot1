from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands = ["start"]))
async def start_handler(message: Message):
    print(f"[LOG] пользователь {message.from_user.id}")
    await message.answer("Салам")

# dp.run_polling()
async def main():
    await dp.start_polling(bot)



run(main()) # запускает цикл событий ()