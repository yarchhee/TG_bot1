import asyncio
from idlelib.undo import Command
from time import sleep

from click import command

from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery


async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()




    # Проект «Опросник»
    # Сценарий: Сбор данных о пользователе (анкета из 3-х вопросов).
    # Твоя задача:
    # Пользователь жмет «Начать тест». Бот присылает первый вопрос.
    # Под вопросом кнопки с вариантами ответа
    # После нажатия на кнопку идет переход на следующий вопрос
    # После третьего вопроса отправляется весь тест с ответами в формате:
    # 1 вопрос:
    # Какой результат деления на 10
    # ответ: {ответ человека}
    # 2 вопрос:
    # Какой результат деления на 10
    # ответ: {ответ человека}
    # 3 вопрос:
    # Какой результат деления на 10
    # ответ: {ответ человека}

    start_test_btn = KeyboardButton(
        text = "Начать тест"
    )

    menu_buttons = ReplyKeyboardMarkup(
        keyboard = [[start_test_btn],]
    )
    questions = [
        {"Какое из этих семи чудес света находилось в Египте и сохранилось до наших дней?":
             {
                 "Пирамида Хеопса": True,
                 "Висячие сады Семирамиды": False,
                 "Колосс Родосский": False
             }
         },
        {"Как звали французскую героиню, ставшую символом освобождения во время Столетней войны?": "Жанна д’Арк"},
        {"Какой мореплаватель возглавил первую в истории экспедицию, совершившую кругосветное путешествие?": "Фернан Магеллан"},
    ]
    counter = 0
    @dp.message(Command(commands="start"))
    async def start_handler(message: Message):
        await message.answer(
            "Начинаем тест, нажмите начать тест",
            reply_markup = menu_buttons
        )

    @dp.message(F.text == "Начать тест")
    async def start_test_handler(message: Message):

        answ = list(questions[0].keys())
        text = list(questions[0].values())[0]

        answ_1_btn = InlineKeyboardButton(
            text = text,
            callback_data = "question"
        )
        answ_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[answ_1_btn]]
        )

        await message.answer(
            answ[0],
            reply_markup=answ_keyboard
        )

    @dp.callback_query(F.data.startswith("question"))
    async def absw_handler(callback: CallbackQuery):
        nonlocal counter
        counter += 1

        answ = list(questions[counter].keys())[0]
        text = list(questions[counter].values())[0]
        answ_1_btn = InlineKeyboardButton(
            text = text,
            callback_data = "question"
        )
        answ_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[answ_1_btn]]
        )
        await callback.message.answer(text = answ, reply_markup=answ_keyboard)

        #Доделать словарь
        #добавить кнопки (создать список перебрать варианты и добавить в него кнопки с вариантами)
        #Сделать вывод после 3го ответа


    await dp.start_polling(bot)
    # asyncio.sleep()

print("[LOG] Бот запущен")
run(main()) #запускает цикла событий (dp)