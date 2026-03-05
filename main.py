from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.filters import Command
from aiogram.types import Message
from requests import get

# dp.run_polling()


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    @dp.message(Command(commands=["catfact"]))
    async def get_cat_fact(message: Message):
        print(f"[LOG] Пользователь {message.from_user.id} запросил /catfact")
        response = get("https://catfact.ninja/fact")
        print(f'[LOG] получен результат со статусом {response.status_code} ')
        response_json = response.json()
        await message.answer(response_json["fact"])

    @dp.message(Command(commands=["start"]))
    async def start_handler(message: Message):
        print(f"[LOG] Пользователь {message.from_user.id} нажал кнопку /start")
        await message.answer("Салам")
    await dp.start_polling(bot)

    @dp.message(Command(commands=["breeds"]))
    async def send_breed(message: Message):
        response = get("https://catfact.ninja/breeds")
        response_json = response.json()
        print(response_json["data"][0]["country"])
        print(response_json["data"][0]["breed"])
    @dp.message()
    async def message_handler(message: Message):
        print(f"[LOG] Пользователь написал какую - то ерунду")
        await message.answer("Я тебя не понимаю")

print(f"[LOG] Бот запущен")
run(main()) # запускает цикл событий