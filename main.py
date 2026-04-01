from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand, ReplyKeyboardRemove, \
    inline_keyboard_button, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command


async def set_commands(bot):
    commands = [
        BotCommand(command="/start", description="Эта команда начинает бот"),
        BotCommand(command="/help", description='Эта команда помогает'),
        BotCommand(command='/neperejivay', description='эта команда чилит')
    ]
    await bot.set_my_commands(commands)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    btn_1 = InlineKeyboardButton(
        text = "Пицца",
        callback_data="food_1"
    )

    btn_2 = InlineKeyboardButton(
        text = "Суши",
        callback_data = "food_2"
    )

    # btn_3 = InlineKeyboardButton(
    #     text="Суп",
    #     url=""
    # )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[btn_1, btn_2]]
    )

    @dp.message(F.text)
    async def text_handler(message: Message):
        text = message.text
        await message.answer("Вот клава", reply_markup=keyboard)

    @dp.callback_query(F.data.startswit('food'))
    async def callback_handler(callback: CallbackQuery):
        # callback.answer
        # callback.message.answer()
        # await callback.message.edit_text("Ваш заказ оформлен")
        data = callback.data
        if data == "food_1":
            await callback.message.answer("Вам отправили пиццу")
        if data == "food_2":
            await callback.message.answer("Вам отправили суши")
        print(data)

    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
# if name == '__main__':
run(main()) # запускает цикла событий(dispatcher)