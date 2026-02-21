
# GET - на получение данных с серверов - html / JSON
# POST - отправляем данные на севрер или сохраняем
# 200 - ура 201
# 404 500 412
# response = requests.get("https://google.com")
# print(response.text)

# API = f"https://api.telegram.org/bot{bot_token}/getMe"

import requests
from config import Config, load_config, TgBot
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandObject
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

@dp.message(Command(commands=['breeds']))
async def show_breeds(message: Message):
    result = requests.get("https://dog.ceo/api/breeds/list/all")
    result_json = result.json()
    dogs_types = result_json["message"].keys()
    s = "\n".join(list(dogs_types)[:30])
    await message.answer(s)

@dp.message(Command(commands=['dog']))
async def answer_dog(message: Message, command: CommandObject):
    print(command.args)
    if command.args :
        s = requests.get(f"https://dog.ceo/api/breed/{command.args}/images/random")
    else:
        s = requests.get(f"https://dog.ceo/api/breeds/image/random")
    json_s = s.json()
    print(json_s)

    if json_s.get("status") == "success":
        # print(json_s.get("message"))
        await message.answer_photo(photo=json_s.get("message"))
    else:
        await message.answer("Не могу так")
    print(s.content)
@dp.message()
async def send_echo(message: Message):
    await message.reply(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



