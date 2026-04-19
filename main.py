from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
)
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command
from handlers import router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    btn_1 = KeyboardButton(text = "📚 Наши курсы")
    btn_2 = KeyboardButton(text = "ℹ️ О нас")
    btn_3 = KeyboardButton(text = "💼 Примеры проектов")
    btn_4 = InlineKeyboardButton(text = "📘 ОГЭ по информатике", callback_data='course_1')
    btn_5 = InlineKeyboardButton(text = "📗 ЕГЭ по информатике",callback_data='course_2')
    btn_6 = InlineKeyboardButton(text = "🐍 Python", callback_data='course_3')
    btn_7 = InlineKeyboardButton(text = "✍️ Записаться", callback_data='zapis_da')
    btn_8 = InlineKeyboardButton(text="◀️ Назад", callback_data='zapis_nazad')
    menu_buttons = ReplyKeyboardMarkup(keyboard=[[btn_1], [btn_2], [btn_3]], resize_keyboard=True)
    inkeyboard_1 = InlineKeyboardMarkup(inline_keyboard=[[btn_4], [btn_5], [btn_6]])
    inkeyboard_2 = InlineKeyboardMarkup(inline_keyboard=[[btn_7],[btn_8]])



    @dp.message(Command("start"))
    async def start_handler(message: Message):
        await message.answer("Приветствую вас в боте! Выберите то, что вам нужно.", reply_markup = menu_buttons)

    @dp.message(F.text == "📚 Наши курсы")
    async def cours_handler(message : Message):
        await message.answer("На данный момент доступны к записи вот эти курсы. Нажмите на понравившийся", reply_markup = inkeyboard_1)


    @dp.callback_query(F.data.startswith("course"))
    async def callback_handler(callback: CallbackQuery):
        data = callback.data
        if data == "course_1":
            await callback.message.edit_text("Программа предназначена для учеников 9 классов сдающих ОГЭ, длительность программы - 1 год.\n Стоимость обучения : 2000 р. \n 90% наших учеников получили МАКСИМАЛЬНЫЙ балл в прошлом году! "
                                             , reply_markup = inkeyboard_2)
        if data == "course_2":
            await callback.message.edit_text("Программа предназначена для учеников 11 классов сдающих ЕГЭ, длительность программы - 1 год.\n Стоимость обучения : 3000 р. \n 70% наших учеников получили МАКСИМАЛЬНЫЙ балл в прошлом году!", reply_markup = inkeyboard_2)

        if data == "course_3":
            await callback.message.edit_text("Хочешь знать как написать такой же крутой бот? Тогда этот курс для тебя! \n 60 часов обучения - 2500 р.", reply_markup = inkeyboard_2)

    @dp.callback_query(F.data.startswith("zapis"))
    async def zapis_handler(callback: CallbackQuery):
        data = callback.data
        if data == "zapis_da":
            pass
        elif data == "zapis_nazad":
            pass



    await dp.start_polling(bot)


print('[LOG] Бот запущен')
run(main())