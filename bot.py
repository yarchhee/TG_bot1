
# GET - на получение данных с серверов - html / JSON
# POST - отправляем данные на севрер или сохраняем
# 200 - ура 201
# 404 500 412
# response = requests.get("https://google.com")
# print(response.text)

# API = f"https://api.telegram.org/bot{bot_token}/getMe"

import requests
from config import Config, load_config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
config: Config = load_config()
bot_token = config.bot.token

bot = Bot(token=bot_token)

dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def process_start(message: Message):
    await message.answer("Привет! Я твой первый бот!")
# help
@dp.message(Command(commands=['help']))
async def process_help(message: Message):
    await message.answer("Чем тебе помочь?")

@dp.message(Command(commands=['dog']))
async def answer_dog(message: Message):
    s = requests.get("https://dog.ceo/api/breeds/image/random")
    await bot.send_photo(message.chat.id, s.content)
@dp.message()
async def send_echo(message: Message):
    await message.reply(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



