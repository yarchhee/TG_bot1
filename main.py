from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
)
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()


    await dp.start_polling(bot)


print('[LOG] Бот запущен')
run(main())