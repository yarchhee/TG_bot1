from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile,ReplyKeyboardMarkup, KeyboardButton
from asyncio import run
from config import BOT_TOKEN
import os
from aiogram.filters import Command
import asyncio
from random import randint

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    knopka_1 = KeyboardButton(text = 'Команда 1')
    keyboard =  ReplyKeyboardMarkup(keyboard = [[knopka_1]])

    @dp.message(Command(commands = 'start'))
    async def command_start(message: Message):
        await message.answer(
            text = "вот",
            reply_markup = keyboard
        )

    @dp.message(F.text == "Команда 1")
    async def command(message: Message):
        await message.answer(
            text = "ты выбрал первую команду",
            reply_markup = keyboard
        )
    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')


if name == '__main__':
    run(main()) # запускает цикла событий(dispatcher)