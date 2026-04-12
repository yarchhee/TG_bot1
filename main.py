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

    btn_1 = KeyboardButton(text = "📚 Наши курсы")
    btn_2 = KeyboardButton(text = "ℹ️ О нас")
    btn_3 = KeyboardButton(text = "💼 Примеры проектов")
    btn_4 = InlineKeyboardButton(text = "📘 ОГЭ по информатике", callback_data='course_1')
    btn_5 = InlineKeyboardButton(text = "📗 ЕГЭ по информатике",callback_data='course_2')
    btn_6 = InlineKeyboardButton(text = "🐍 Python", callback_data='course_3')
    menu_buttons = ReplyKeyboardMarkup(keyboard=[[btn_1], [btn_2], [btn_3]], resize_keyboard=True)
    inkeyboard_1  = InlineKeyboardMarkup(keyboard=[[btn_4], [btn_5], [btn_6]])


    @dp.message(Command("start"))
    async def start_handler(message: Message):
        await message.answer("Приветствую вас в боте! Выберите то, что вам нужно.", reply_markup = menu_buttons)

    @dp.message(F.text == "📚 Наши курсы")
    async def cours_handler(message : Message):
        await message.answer("На данный момент доступны к записи вот эти курсы. Нажмите на понравившийся")

    @dp.callback_query(F.data.startswith("course"))
    async def callback_handler(call: CallbackQuery):
        data = callback.data
        if data == "course_1":
            await callback.message.answer("")

    await dp.start_polling(bot)


print('[LOG] Бот запущен')
run(main())